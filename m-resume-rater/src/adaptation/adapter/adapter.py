from bs4 import BeautifulSoup

from src.resume import Part, Entity, Resume, Id as ResumeId


# todo test
class Adapter:
    def __init__(self, content: str) -> None:
        self._soup = BeautifulSoup(content, 'html.parser')
        self._extractors = {}

    def extractor(self, entity: Entity, extractor):
        self._extractors[entity] = extractor

    def compute_resume(self, resume_id: ResumeId) -> Resume:
        # todo impl
        pass


if __name__ == '__main__':
    pass
