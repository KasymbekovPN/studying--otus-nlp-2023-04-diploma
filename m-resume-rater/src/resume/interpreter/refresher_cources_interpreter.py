from src.result import Result
from src.resume.interpreter import BaseInterpreter


class RefresherCoursesInterpreter(BaseInterpreter):
    def raw(self) -> Result:
        refresher_courses = self.resume.refresher_courses
        return Result.simple_fail('resume.refresher-courses.absence', id=self.resume.resume_id) \
            if refresher_courses is None \
            else Result.ok(refresher_courses)
