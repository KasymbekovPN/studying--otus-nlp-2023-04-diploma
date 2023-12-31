
class Status:
    def __init__(self, template: str, **kwargs) -> None:
        self._template = template
        self._args = kwargs

    def __repr__(self) -> str:
        return f'Status {{ template: {self._template}, args: {self._args} }}'

    def __eq__(self, other) -> bool:
        return isinstance(other, self.__class__) \
            and self.template == other.template \
            and self.args == other.args

    @property
    def template(self) -> str:
        return self._template

    @property
    def args(self) -> dict:
        return self._args


class Result:
    def __init__(self, success: bool, value, statuses: list[Status]) -> None:
        self._success = success if success is not None else False
        self._value = value
        self._statuses = statuses if statuses is not None else []

    def __repr__(self) -> str:
        return f'Result {{ success: {self.success}, value: {self.value}, statuses: {self.statuses} }}'

    def __eq__(self, other) -> bool:
        return isinstance(other, self.__class__) \
            and self.success == other.success \
            and self.value == other.value \
            and self.statuses == other.statuses

    @property
    def success(self) -> bool:
        return self._success

    @property
    def value(self):
        return self._value

    @property
    def statuses(self) -> list[Status]:
        return self._statuses

    @staticmethod
    def ok(value):
        return Result(True, value, [])

    @staticmethod
    def fail(status: Status):
        return Result(False, None, [status])

    @staticmethod
    def simple_fail(template: str, **kwargs):
        return Result(False, None, [Status(template, **kwargs)])

    @staticmethod
    def full(success: bool, value, statuses: list[Status]):
        return Result(success, value, statuses)