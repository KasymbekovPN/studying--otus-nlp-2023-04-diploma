import torch

from sentence_transformers import SentenceTransformer, util
from src.resume import Part
from src.utils import NWordsComputer, get_torch_device
from src.model.corpus import Corpus
from src.utils.kwargs_util import check_type_and_get_or_default, ArgDescription
from src.utils.limited_sorted_holder import Holder


# todo test
class Model:
    THRESHOLD_DESCR = ArgDescription('threshold', float, 0.0)
    TOP_K_DESCR = ArgDescription('top_k', int, 1)
    TOP_BEST_DESCR = ArgDescription('top_best', int, 10)

    def __init__(self,
                 embedder: SentenceTransformer,
                 corpus: Corpus,
                 n_words_computer: NWordsComputer) -> None:
        self._embedder = embedder
        self._corpus = corpus
        self._n_words_computer = n_words_computer

    def execute(self, part: Part, **kwargs) -> tuple:
        threshold = check_type_and_get_or_default(kwargs, self.THRESHOLD_DESCR)
        top_k = check_type_and_get_or_default(kwargs, self.TOP_K_DESCR)
        holder = Holder(check_type_and_get_or_default(kwargs, self.TOP_BEST_DESCR))
        counter = 0
        total_score = 0.0

        for sub in self._n_words_computer.compute(part.value):
            top_results = self._calculate_top_results(sub, top_k)
            for score, idx in zip(top_results[0], top_results[1]):
                counter += 1
                if score >= threshold:
                    score_item = score.item()
                    total_score += score_item
                    holder.add(score_item, (score_item, sub, self._corpus.values[idx]))

        return total_score / counter, holder.get()

    def _calculate_top_results(self, sub: str, top_k: int):
        sub_embedding = self._embedder.encode(sub, convert_to_tensor=True)
        cos_scores = util.cos_sim(sub_embedding, self._corpus.embeddings)[0]
        return torch.topk(cos_scores, k=top_k)
