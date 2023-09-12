from bs4 import BeautifulSoup

from src.resume import Entity, Resume, Id as ResumeId


# todo test
class Adapter:
    def __init__(self) -> None:
        self._extractors = {}

    def extractor(self, entity: Entity, extractor):
        self._extractors[entity] = extractor

    def compute_resume(self, resume_id: ResumeId, content: str) -> Resume:
        soup = BeautifulSoup(content, 'html.parser')
        parts = {}
        for entity, extractor in self._extractors.items():
            parts[entity.value[1]] = extractor(soup)
        return Resume(resume_id, **parts)
