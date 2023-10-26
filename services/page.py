from .http import Http
from models.tag import Tag, FactoryTag

from requests import Response
from bs4 import BeautifulSoup
from typing import List


class Page:
    _path: str
    _soup_page: BeautifulSoup

    error: str

    def __init__(self, path: str) -> None:
        self._path = path

    def _do_soup(self, page: Response) -> bool:
        try:
            self._soup_page = BeautifulSoup(page.content, "html.parser")
        except Exception as e:
            self.error = f"error on parsing page: {e}"
            return False
        
        return True

    async def download_page(self) -> bool:
        try:
            page = Http.get(self._path)
        except Exception as e:
            self.error = str(e)
            return False
        
        return self._do_soup(page=page)
    
    def submit_form(self, code: str) -> bool:
        csrf = FactoryTag.create_csrf_code(self._soup_page)

        try:
            page = Http.post(
                self._path,
                {"csrf": csrf.value, "codigo": code}
            )
        except Exception as e:
            self.error = str(e)
            return False
        
        if not self._do_soup(page=page):
            return False

        return True
    
    def get_links(self) -> List[Tag]:
        return FactoryTag.create_links(self._soup_page)
