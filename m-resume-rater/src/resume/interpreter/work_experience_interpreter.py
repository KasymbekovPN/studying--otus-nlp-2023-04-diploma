from src.result import Result
from src.resume.interpreter import BaseInterpreter


class WorkExperienceInterpreter(BaseInterpreter):
    def raw(self) -> Result:
        work_experience = self.resume.work_experience
        return Result.simple_fail('resume.work-experience.absence', id=self.resume.resume_id) \
            if work_experience is None \
            else Result.ok(work_experience)
