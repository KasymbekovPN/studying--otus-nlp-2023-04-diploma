from src.result import Result
from src.resume import Resume
from src.utils import NGramsComputer, NWordsComputer


# todo ???
class BaseInterpreter:
    NGRAMS_COMPUTER_KEY = 'ngrams'
    NWORDS_COMPUTER_KEY = 'nwords'

    def __init__(self, resume: Resume, **kwargs) -> None:
        self._resume = resume
        self._ngrams_computer = BaseInterpreter.check_ngrams_computer(kwargs)
        self._nwords_computer = BaseInterpreter.check_nwords_computer(kwargs)

    @property
    def resume(self):
        return self._resume

    def raw(self) -> Result:
        return Result.simple_fail('interpreter.getting.raw.unsupported', class_name=self.__class__.__name__)

    def ngrams(self) -> Result:
        result = self.raw()
        if not result.success:
            return result

        if self._ngrams_computer is None:
            return Result.simple_fail(
                'interpreter.getting.ngrams.computer-absence',
                class_name=self.__class__.__name__)

        return self._ngrams_computer.compute(result.value)

    def nwords(self) -> Result:
        result = self.raw()
        if not result.success:
            return result

        if self._nwords_computer is None:
            return Result.simple_fail(
                'interpreter.getting.nwords.computer-absence',
                class_name=self.__class__.__name__)

        return self._nwords_computer.compute(result.value)

    @staticmethod
    def check_ngrams_computer(args: dict) -> NGramsComputer | None:
        key = BaseInterpreter.NGRAMS_COMPUTER_KEY
        return args.get(key) if key in args and isinstance(args.get(key), NGramsComputer) else None

    @staticmethod
    def check_nwords_computer(args: dict) -> NWordsComputer | None:
        key = BaseInterpreter.NWORDS_COMPUTER_KEY
        return args.get(key) if key in args and isinstance(args.get(key), NWordsComputer) else None
