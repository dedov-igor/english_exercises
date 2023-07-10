from spacy.tokens import Token


def replace_word(sentence: str, token: Token, sentence_offset: int, replace_with: str = '*****'):
    return sentence[:token.idx - sentence_offset] + replace_with + sentence[token.idx + len(token.text) - sentence_offset:]

