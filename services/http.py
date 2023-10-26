from requests import Response, request


class Http:
    _BASE: str = "https://simpleenergy.com.br"
    _CUSTOM_HEADERS: dict = {"User-Agent": "Safari/537.36"}

    @staticmethod
    def _do_request(
        method: str,
        path: str,
        data: dict = None
    ) -> Response:
        url = f"{Http._BASE}{path}"

        resp = request(
            method=method,
            url=url,
            headers=Http._CUSTOM_HEADERS,
            data=data
        )

        if resp.status_code != 200:
            raise Exception(
                f"couldn't get response for {path}: status {resp.status_code}"
            )
        
        return resp
    
    @staticmethod
    def get(path: str) -> Response:
        return Http._do_request("GET", path)

    @staticmethod
    def post(path: str, data: dict) -> Response:
        return Http._do_request("POST", path, data)
