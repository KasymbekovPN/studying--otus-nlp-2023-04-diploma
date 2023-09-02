import validators

from enum import Enum

from src.result import Result, Status


class IdKind(Enum):
    URL = 0


class Id:
    def __init__(self, kind: IdKind, value) -> None:
        self._kind = kind
        self._value = value

    def __repr__(self):
        return f'ResumeId {{ kind: {self.kind}, value: {self.value} }}'

    # todo checking of types -- through decorator ?
    def __eq__(self, other):
        return isinstance(other, self.__class__) \
            and self.kind == other.kind \
            and self.value == other.value

    @property
    def kind(self) -> IdKind:
        return self._kind

    @property
    def value(self):
        return self._value

    @staticmethod
    def url(value: str) -> Result:
        return Result.ok(Id(IdKind.URL, value)) \
            if validators.url(value) \
            else Result.fail(Status('resume.id.creation.bad-url', url=value))
