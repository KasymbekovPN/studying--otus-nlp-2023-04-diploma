from src.result import Result
from src.resume.interpreter import BaseInterpreter


# todo ???
class CVInterpreter(BaseInterpreter):
    def raw(self) -> Result:
        cv = self.resume.cv
        return Result.simple_fail('resume.cv.absence', id=self.resume.resume_id) \
            if cv is None \
            else Result.ok(cv)
