
# todo test it
class NWordsComputer:
    MIN_SIZE = 1
    MAX_SIZE = 100
    DEFAULT_SIZE = 5

    def __init__(self, min_border=None, max_border=None) -> None:
        self._min = self._check_and_get_min(min_border)
        _max = self._check_and_get_max(max_border, self._min)
        self._ranges = [i for i in range(self._min, _max + 1)]

    def compute(self, sentences: tuple) -> tuple:
        result = []
        for sentence in sentences:
            sub_sentences = set()
            words = sentence.split(' ')
            sentence_len = len(words)
            for range_border in self._ranges:
                for start in range(sentence_len):
                    sub_words = self._create_line(words, start, range_border)
                    if len(sub_words) >= self._min:
                        sub_sentences.add(' '.join(sub_words))
            result.append(sub_sentences)
        return tuple(result)

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


# todo del
if __name__ == '__main__':
    from src.resume import Id as ResumeId, Entity
    from src.adaptation.adapter.adapter import Adapter
    from src.adaptation.extractor.hh.work_experience.extractor import extract_work_experience_from_hh
    from src.adaptation.extractor.hh.skills.extractor import extract_skills_from_hh
    from src.adaptation.extractor.hh.specialization.extractor import extract_specialization_from_hh
    from src.adaptation.extractor.hh.position.extractor import extract_position_from_hh

    path = 'C:\\Users\\KasymbekovPN\\projects\\_temporary\\resumes\\resume5.html'
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    adapter = Adapter()
    adapter.extractor(Entity.WORK_EXPERIENCE, extract_work_experience_from_hh)
    # adapter.extractor(Entity.SKILLS, extract_skills_from_hh)
    # adapter.extractor(Entity.SPECIALIZATION, extract_specialization_from_hh)
    # adapter.extractor(Entity.POSITION, extract_position_from_hh)

    resume = adapter.compute_resume(ResumeId.url('https://10.0.0.1').value, content)
    print(resume.get(Entity.WORK_EXPERIENCE))

    computer = NWordsComputer(5, 7)
    result = computer.compute(resume.get(Entity.WORK_EXPERIENCE).value)

    # words = ['', 'Я', 'написал', 'бэкенд', 'для', 'сервиса,', 'который', 'позволит', 'пользователям', 'делиться', 'информацией', 'об', 'интересных', 'событиях', 'и', 'находить', 'компанию', 'для', 'участия', 'в', 'них']
    # s = NWordsComputer._create_line(words, 3, 5)
    # print(s)
    # s = NWordsComputer._create_line(words, 3, 50)
    # print(s)
    pass
