from src.result import Result
from src.resume.interpreter import BaseInterpreter


# todo ???
class EducationInterpreter(BaseInterpreter):
    def raw(self) -> Result:
        education = self.resume.education
        return Result.simple_fail('resume.education.absence', id=self.resume.resume_id) \
            if education is None \
            else Result.ok(education)
