import re

from bs4 import BeautifulSoup
from src.resume import Part


REPLACEMENT = [
    (r'http\S+', ' '),
    (r'<a href=.*</a>', ' '),
    (r'<[0-9a-zA-Z="_:/. -]+>', ' '),
    (r'</[a-zA-Z]+>', ' '),
    (r'\n', ''),
    (r',', ', '),
    (r' +:', ': '),
    (r' +', ' ')
]


# todo: test
def extract_work_experience_from_hh(soup: BeautifulSoup) -> Part:
    tags = soup.find_all('div', {'data-qa': 'resume-block-experience-description'})
    result = []
    for tag in tags:
        text = tag.text
        for replace_tuple in REPLACEMENT:
            text = re.sub(replace_tuple[0], replace_tuple[1], text)
        result = result + text.split('.')
    return Part(*result)


# todo del
if __name__ == '__main__':
    path = 'C:\\Users\\KasymbekovPN\\projects\\_temporary\\resumes\\resume5.html'
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')
    part = extract_work_experience_from_hh(soup)
    print(part)
