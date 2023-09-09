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
    def __init__(self, embeddings):
        self._embeddings = embeddings

    @property
    def embeddings(self):
        return self._embeddings

    @staticmethod
    def create(source, encoder, extractor=extract_from_text_file, handler=prepare_simple_list_content):
        content = extractor(source)
        if content is None:
            return Result.simple_fail('corpus.source.non-exist', source=source)
        sentences = handler(content)
        if len(sentences) == 0:
            return Result.simple_fail('corpus.source.empty', source=source)

        corpus_embeddings = embedder.encode(sentences, convert_to_tensor=True)
        return Result.ok(Corpus(corpus_embeddings))


# todo del
if __name__ == '__main__':
    path = 'C:\\Users\\KasymbekovPN\\projects\\_temporary\\corpus\\dev_corpus.txt'

    content = extract_from_text_file(path)
    # print(content)

    corpus_value = prepare_simple_list_content(content)
    print(corpus_value)

    PRETRAINED_PATH = 'sentence-transformers/LaBSE'

    print(torch.cuda.is_available())

    def get_device():
        if torch.cuda.is_available():
            print(f'There are {torch.cuda.device_count()} GPU(s) available.')
            print(f'We will use the GPU: {torch.cuda.get_device_name(0)}')
            device = torch.device('cuda')
        else:
            print('No GPU available, using the CPU instead.')
            device = torch.device('cpu')
        return device

    embedder = SentenceTransformer(PRETRAINED_PATH)
    embedder.to(get_device())

    # corpus_embeddings = embedder.encode(corpus_value, convert_to_tensor=True)
    # print(corpus_embeddings.shape)

    result = Corpus.create(path, embedder)
    print(result)


