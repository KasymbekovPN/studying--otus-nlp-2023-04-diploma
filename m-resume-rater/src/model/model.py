import torch
from sentence_transformers import SentenceTransformer, util
from src.rate import Rate
from src.resume import Part
from src.utils import NWordsComputer, get_torch_device
from src.model.corpus import Corpus


# todo impl + test
class Model:
    def __init__(self,
                 embedder: SentenceTransformer,
                 corpus: Corpus,
                 n_words_computer: NWordsComputer,
                 threshold: float) -> None:
        self._embedder = embedder
        self._corpus = corpus
        self._n_words_computer = n_words_computer
        self._top_k = 1 # todo ??? min(5, len(self._corpus))
        self._description_size = 10 # todo !!!
        self._threshold = threshold

    def execute(self, part: Part) -> Rate:
        counter = 0
        total_score = 0.0
        prepared_sub_sentences = self._n_words_computer.compute(part.value)
        for set_ in prepared_sub_sentences:
            # todo del
            # print('+++++++++++++++++++++++++++++++++')
            for sub in set_:
                # todo del
                print('----------------------------')
                print(f'sub: {sub}')
                top_results = self._calculate_top_results(sub)
                print(top_results)

                for score, idx in zip(top_results[0], top_results[1]):
                    counter += 1
                    if score >= self._threshold:
                        total_score += score
                    print(self._corpus.values[idx], "(Score: {:.4f})".format(score))

        print(f'total_score: {total_score}')
        print(f'avg: {total_score / counter}')

        # todo del: it's temporary Rate instance
        temp_rate = Rate(Entity.SKILLS, 'default')
        return temp_rate

    def _calculate_top_results(self, sub: str):
        sub_embedding = self._embedder.encode(sub, convert_to_tensor=True)
        cos_scores = util.cos_sim(sub_embedding, self._corpus.embeddings)[0]
        return torch.topk(cos_scores, k=self._top_k)


# todo del
if __name__ == '__main__':
    from src.resume import Id as ResumeId, Entity
    from src.adaptation.adapter.adapter import Adapter
    from src.adaptation.extractor.hh.work_experience.extractor import extract_work_experience_from_hh

    path = 'C:\\Users\\KasymbekovPN\\projects\\_temporary\\corpus\\dev_corpus.txt'
    pretrained_path = 'sentence-transformers/LaBSE'

    embedder = SentenceTransformer(pretrained_path)
    embedder.to(get_torch_device())
    corpus = Corpus.create(path, embedder).value
    computer = NWordsComputer()

    model = Model(embedder, corpus, computer, 0.0)
    print(model)

    path = 'C:\\Users\\KasymbekovPN\\projects\\_temporary\\resumes\\resume5.html'
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    adapter = Adapter()
    adapter.extractor(Entity.WORK_EXPERIENCE, extract_work_experience_from_hh)

    resume = adapter.compute_resume(ResumeId.url('https://10.0.0.1').value, content)
    part = resume.get(Entity.WORK_EXPERIENCE)

    rate = model.execute(part)
    print(rate)

