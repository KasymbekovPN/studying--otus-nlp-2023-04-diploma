import re

from bs4 import BeautifulSoup
from src.resume import Part


REPLACEMENT = [
    (r'<[0-9a-zA-Z="_:/. -]+>', ' '),
    (r'</[a-zA-Z]+>', ' ')
]


# todo: test
def extract_position_from_hh(soup: BeautifulSoup) -> Part:
    tags = soup.find_all('div', {'data-qa': 'resume-block-experience-position'})
    result = []
    for tag in tags:
        text = tag.text
        for replace_tuple in REPLACEMENT:
            text = re.sub(replace_tuple[0], replace_tuple[1], text)
        result = result + text.split('.')
    return Part(*result)
