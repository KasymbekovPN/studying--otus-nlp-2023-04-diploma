from src.result import Result
from src.resume.interpreter import BaseInterpreter


# todo ???
class ShortAboutInterpreter(BaseInterpreter):
    def raw(self) -> Result:
        short_about = self.resume.short_about
        return Result.simple_fail('resume.short-about.absence', id=self.resume.resume_id) \
            if short_about is None \
            else Result.ok(short_about)

#  todo off ngrams/nwords ???

# todo del
# ------- short_about
# Москва

# , не
# готов
# к
# переезду,
#
# готов
# к
# редким
# командировкам

# Занятость: полная
# занятость

# График
# работы: полный
# день
# ------- short_about
