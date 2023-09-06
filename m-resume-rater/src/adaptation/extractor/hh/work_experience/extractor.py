import re

from bs4 import BeautifulSoup
from src.resume import Part


def extract_work_experience_from_hh(soup: BeautifulSoup) -> Part:
    pass


if __name__ == '__main__':
    path = 'C:\\Users\\KasymbekovPN\\projects\\_temporary\\resumes\\resume5.html'
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')
    tags = soup.find_all('div', {'data-qa': 'resume-block-experience-description'})
    for tag in tags:
        print(10*'-')
        t = tag.text
        t = re.sub(r'http\S+', ' ', t)
        t = re.sub(r'<a href=.*</a>', ' ',  t)
        t = re.sub(r'<[0-9a-zA-Z="_:/. -]+>', ' ', t)
        t = re.sub(r'</[a-zA-Z]+>', ' ', t)
        t = re.sub(r'\n', '', t)
        # t = re.sub(r'\W+', ' ', t)
        print(t)
