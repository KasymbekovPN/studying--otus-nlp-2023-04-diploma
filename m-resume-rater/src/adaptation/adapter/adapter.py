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


# todo del
if __name__ == '__main__':
    from src.adaptation.extractor.hh.work_experience.extractor import extract_work_experience_from_hh
    from src.adaptation.extractor.hh.skills.extractor import extract_skills_from_hh
    from src.adaptation.extractor.hh.specialization.extractor import extract_specialization_from_hh
    from src.adaptation.extractor.hh.position.extractor import extract_position_from_hh

    path = 'C:\\Users\\KasymbekovPN\\projects\\_temporary\\resumes\\resume5.html'
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    adapter = Adapter()
    adapter.extractor(Entity.WORK_EXPERIENCE, extract_work_experience_from_hh)
    adapter.extractor(Entity.SKILLS, extract_skills_from_hh)
    adapter.extractor(Entity.SPECIALIZATION, extract_specialization_from_hh)
    adapter.extractor(Entity.POSITION, extract_position_from_hh)

    resume = adapter.compute_resume(ResumeId.url('https://10.0.0.1').value, content)
    print(resume)
