import torch

from sentence_transformers import SentenceTransformer
from src.result import Result


def extract_from_text_file(source) -> str | None:
    try:
        with open(source, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as ex:
        print(ex)
        return None


def prepare_simple_list_content(content: str) -> list:
    return [item.lower() for item in content.split('\n') if len(item) > 0]


# todo text
class Corpus:
    def __init__(self, values, embeddings):
        self._values = values
        self._embeddings = embeddings

    def __len__(self) -> int:
        return len(self._embeddings)

    @property
    def values(self):
        return self._values

    @property
    def embeddings(self):
        return self._embeddings

    @staticmethod
    def create(source, embedder, extractor=extract_from_text_file, handler=prepare_simple_list_content):
        content = extractor(source)
        if content is None:
            return Result.simple_fail('corpus.source.non-exist', source=source)
        sentences = handler(content)
        if len(sentences) == 0:
            return Result.simple_fail('corpus.source.empty', source=source)

        corpus_embeddings = embedder.encode(sentences, convert_to_tensor=True)
        return Result.ok(Corpus(sentences, corpus_embeddings))
