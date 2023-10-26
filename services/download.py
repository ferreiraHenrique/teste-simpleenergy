from .http import Http

import os


class Download:
    _external_path: str
    _folder_name: str
    _file_name: str

    def __init__(
        self,
        external_path: str,
        out_folder_name: str,
        out_file_name: str,
    ) -> None:
        self._external_path = external_path
        self._folder_name = out_folder_name
        self._file_name = out_file_name

        if not os.path.exists(out_folder_name):
            os.mkdir(out_folder_name)

    async def do_download(self) -> bool:
        try:
            resp = Http.get(self._external_path)
        except Exception as e:
            return False   

        output_path = f"{self._folder_name}/{self._file_name}"
        open(output_path, "wb").write(resp.content)

        return True
