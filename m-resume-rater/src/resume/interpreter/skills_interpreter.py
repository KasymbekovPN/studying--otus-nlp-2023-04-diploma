from src.result import Result
from src.resume.interpreter import BaseInterpreter


class SkillsInterpreter(BaseInterpreter):
    def raw(self) -> Result:
        skills = self.resume.skills
        return Result.simple_fail('resume.skills.absence', id=self.resume.resume_id) \
            if skills is None \
            else Result.ok(skills)

    #  todo off ngrams/nwords ???
