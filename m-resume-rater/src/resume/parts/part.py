
class Part:
    def __init__(self, *args):
        self._value = tuple([s for s in args if isinstance(s, str) and len(s) > 0])

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} {self.value}'

    def __eq__(self, other) -> bool:
        return isinstance(other, self.__class__) and self.value == other.value

    @property
    def value(self) -> tuple:
        return self._value
