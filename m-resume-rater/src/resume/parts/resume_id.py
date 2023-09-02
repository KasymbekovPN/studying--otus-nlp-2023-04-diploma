import validators

from enum import Enum

from src.result.result import Result, Status


class ResumeIdKind(Enum):
    URL = 0


class ResumeId:
    def __init__(self, kind: ResumeIdKind, value) -> None:
        self._kind = kind
        self._value = value

    def __repr__(self):
        return f'ResumeId {{ kind: {self.kind}, value: {self.value} }}'

    # todo checking of types -- through decorator ?
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.kind == other.kind and self.value == other.value

    @property
    def kind(self) -> ResumeIdKind:
        return self._kind

    @property
    def value(self):
        return self._value

    @staticmethod
    def url(value: str) -> Result:
        return Result.ok(ResumeId(ResumeIdKind.URL, value)) \
            if validators.url(value) \
            else Result.fail(Status('resume.id.creation.bad-url', url=value))
