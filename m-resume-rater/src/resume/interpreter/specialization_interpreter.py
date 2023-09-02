from src.result import Result
from src.resume.interpreter import BaseInterpreter


class SpecializationInterpreter(BaseInterpreter):
    def raw(self) -> Result:
        specialization = self.resume.specialization
        return Result.simple_fail('resume.specialization.absence', id=self.resume.resume_id) \
            if specialization is None \
            else Result.ok(specialization)

    #  todo off ngrams/nwords ???
