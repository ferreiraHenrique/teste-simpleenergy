from dataclasses import dataclass
from bs4 import BeautifulSoup
from typing import List


@dataclass
class Tag:
    value: str

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k in ["value", "href"]:
                self.value = v
                
class FactoryTag:
    @staticmethod
    def create_csrf_code(soup: BeautifulSoup) -> Tag:
        csrf_input = soup.find("input", {"name": "csrf"})
        return Tag(**csrf_input.attrs)
    
    @staticmethod
    def create_links(soup: BeautifulSoup) -> List[Tag]:
        links = soup.find_all("a")
        return list(map(
            lambda l: Tag(**l.attrs),
            links
        ))
