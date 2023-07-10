from pathlib import Path


def load_data(path: Path, spacy_model):
    sentences = []
    for line in path.read_text(encoding='UTF-8').splitlines():
        if len(line.rstrip()) > 0:
            for sent in spacy_model(line).sents:
                if len(str(sent).rstrip()) > 1:
                    sentences.append(sent)
    return sentences