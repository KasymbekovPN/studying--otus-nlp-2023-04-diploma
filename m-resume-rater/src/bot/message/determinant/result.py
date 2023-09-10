from enum import Enum

from src.bot.engine.strategy import (
    BaseEngineStrategy,
    UnknownCommandEngineStrategy,
    TextEngineStrategy
)
from src.adaptation.adapter.adapter import Adapter


class ResultKind(Enum):
    UNKNOWN = -1, 'unknown kind'
    UNKNOWN_COMMAND = 0, 'unknown command kind'
    SPEC_COMMAND = 1, 'special command kind'
    TEXT = 2, 'text kind'


class Result:
    def __init__(self,
                 kind: ResultKind,
                 text: str | None,
                 strategy=BaseEngineStrategy()) -> None:
        self._kind = kind
        self._text = text
        self._strategy = strategy

    def __repr__(self):
        return f'{{kind: {self.kind.value[1]}, text: {self.text}, strategy: {self.strategy.__class__.__name__} }}'

    @property
    def kind(self):
        return self._kind

    @property
    def text(self):
        return self._text

    @property
    def strategy(self):
        return self._strategy

    @staticmethod
    def create_for_unknown(text: str):
        return Result(ResultKind.UNKNOWN, text)

    @staticmethod
    def create_for_spec_command(text: str, strategy: BaseEngineStrategy):
        return Result(ResultKind.SPEC_COMMAND, text, strategy)

    @staticmethod
    def create_for_unknown_command(text: str):
        return Result(ResultKind.UNKNOWN_COMMAND, text, UnknownCommandEngineStrategy())

    @staticmethod
    def create_for_text(text: str, adapter: Adapter):
        return Result(ResultKind.TEXT, text, TextEngineStrategy(adapter))
