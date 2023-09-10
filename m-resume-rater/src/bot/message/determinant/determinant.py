import re

from src.bot.message.determinant.result import Result
from src.bot.engine.strategy import BaseEngineStrategy


class BaseDeterminant:
    def __call__(self, *args, **kwargs) -> Result | None:
        text = kwargs.get('text') if 'text' in kwargs else None
        return self._determinate(text)

    def _determinate(self, text: str | None) -> Result | None:
        return Result.create_for_unknown(text)


class SpecificCommandDeterminant(BaseDeterminant):
    def __init__(self, command: str, strategy: BaseEngineStrategy) -> None:
        self._command = command
        self._strategy = strategy

    def _determinate(self, text: str | None) -> Result | None:
        if self._command == text:
            return Result.create_for_spec_command(text, self._strategy)
        return None


class AnyCommandDeterminant(BaseDeterminant):
    def __init__(self):
        self._re = re.compile('/[a-z][a-zA-Z0-9_]+')

    def _determinate(self, text: str | None) -> Result | None:
        if text is not None:
            match = self._re.match(text)
            if match is not None and len(text) == self._re.match(text).span()[1]:
                return Result.create_for_unknown_command(text)
        return None


class TextDeterminant(BaseDeterminant):
    def _determinate(self, text: str | None) -> Result | None:
        return None if text is None else Result.create_for_text(text)


class DefaultDeterminant(BaseDeterminant):
    pass
