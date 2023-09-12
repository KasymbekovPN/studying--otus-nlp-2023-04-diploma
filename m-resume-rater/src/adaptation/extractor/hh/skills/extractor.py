import re

from bs4 import BeautifulSoup
from src.resume import Part


REPLACEMENT = [
    (r'<[0-9a-zA-Z="_:/. -]+>', ' '),
    (r'</[a-zA-Z]+>', ' '),
    (r' +', ' ')
]


# todo: test
def extract_skills_from_hh(soup: BeautifulSoup) -> Part:
    elements = soup.find_all('div', {'data-qa': 'skills-table'})

    result = []
    for element in elements:
        tags = element.find_all('span', {'data-qa': 'bloko-tag__text'})
        for tag in tags:
            text = tag.text
            for replace_tuple in REPLACEMENT:
                text = re.sub(replace_tuple[0], replace_tuple[1], text)
            result.append(text)
    return Part(*result)
