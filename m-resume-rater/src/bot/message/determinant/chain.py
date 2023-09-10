from src.bot.message.determinant.determinant import (
    BaseDeterminant,
    DefaultDeterminant
)


class Chain:
    _DEFAULT_DETERMINANT = DefaultDeterminant()

    def __init__(self, determinants: list[BaseDeterminant]):
        self._determinants = determinants

    def __call__(self, *args, **kwargs):
        text = kwargs.get('text') if 'text' in kwargs else None

        for determinant in self._determinants:
            result = determinant(text=text)
            if result is not None:
                return result

        return self._DEFAULT_DETERMINANT(text=text)
