import re

from bs4 import BeautifulSoup
from src.resume import Part


REPLACEMENT = [
    (r', ', ',')
]


# todo: test
def extract_specialization_from_hh(soup: BeautifulSoup) -> Part:
    tags = soup.find_all('li', {'data-qa': 'resume-block-position-specialization'})
    s = set()
    for tag in tags:
        text = tag.text
        for replace_tuple in REPLACEMENT:
            text = re.sub(replace_tuple[0], replace_tuple[1], text)
        s = text.lower().split(',')
    return Part(*s)
