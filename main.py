from models.tag import Tag
from services.page import Page
from services.download import Download

from typing import List
import asyncio
import os
import shutil


async def handle_download(code: str, link: Tag):
    print(f"Initiating download file: {link.value}")

    external_path = f"/teste/{link.value}"
    download = Download(
        external_path,
        out_folder_name=code,
        out_file_name=link.value
    )
    if not (await download.do_download()):
        print(f"Error on download file: {link.value}")
        return
    
    print(f"Done download file: {link.value}")

async def handle_code(code: str):
    print(f"Initiating code: {code}")
    page = Page(path="/teste/")
    if not (await page.download_page()):
        print(page.error)
        return

    if not page.submit_form(code):
        print(page.error)
        return
    
    downloads = (handle_download(code, link) for link in page.get_links())
    await asyncio.gather(*downloads)

async def main(codes: List[str]):
    for code in codes:
        await handle_code(code)

def init_folder(folder_name: str):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)

if __name__ == "__main__":
    codes = ["321465", "98465"]

    for c in codes:
        init_folder(c)

    asyncio.run(main(codes))