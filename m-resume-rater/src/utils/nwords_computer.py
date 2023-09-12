
# todo test it
class NWordsComputer:
    MIN_SIZE = 1
    MAX_SIZE = 100
    DEFAULT_SIZE = 5

    def __init__(self, min_border=None, max_border=None) -> None:
        self._min = self._check_and_get_min(min_border)
        _max = self._check_and_get_max(max_border, self._min)
        self._ranges = [i for i in range(self._min, _max + 1)]

    def compute(self, sentences: tuple) -> set:
        result = set()
        for sentence in sentences:
            sub_sentences = set()
            words = sentence.split(' ')
            sentence_len = len(words)
            for range_border in self._ranges:
                for start in range(sentence_len):
                    sub_words = self._create_line(words, start, range_border)
                    if len(sub_words) >= self._min:
                        sub_sentences.add(' '.join(sub_words))
            result = result.union(sub_sentences)
        return result

    @classmethod
    def _check_and_get_min(cls, raw_value) -> int:
        return raw_value \
            if isinstance(raw_value, int) and cls.MIN_SIZE <= raw_value <= cls.MAX_SIZE \
            else cls.DEFAULT_SIZE

    @classmethod
    def _check_and_get_max(cls, raw_value, min_size: int) -> int:
        return raw_value if isinstance(raw_value, int) and min_size < raw_value <= cls.MAX_SIZE else min_size

    @staticmethod
    def _create_line(words: list, start: int, size: int) -> list | None:
        words_size = len(words)
        if start >= words_size:
            return None
        return [words[idx] for idx in range(start, size + start) if idx < words_size and len(words[idx]) > 0]
