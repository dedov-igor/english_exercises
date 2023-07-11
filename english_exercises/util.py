import random

from spacy.tokens import Token

from english_exercises.exercise.exercise import Exercise


def replace_word(sentence: str, token: Token, sentence_offset: int, replace_with: str = '*****'):
    return sentence[:token.idx - sentence_offset] + replace_with + sentence[token.idx + len(token.text) - sentence_offset:]


def create_synonym(model, top_words_count, token):
    m = random.randint(0, top_words_count - 1)
    synonym = model.most_similar(token.text.lower(), topn=top_words_count)[m][0]
    synonym = synonym.title() if token.text.istitle() else synonym
    return synonym


def create_antonym(model, top_words_count, token):
    m = random.randint(0, top_words_count - 1)
    antonym = model.most_similar(positive=[token.text.lower(), 'bad'], negative=['good'],
                                 topn=top_words_count)[m][0]
    antonym = antonym.title() if token.text.istitle() else antonym
    return antonym



def selection_of_k_exercises(exercises: list[Exercise], k=10):  # k - количество упражнений включаемых в датасет
    # Выборка k случайных упражнений для добавлениея в датасет
    return random.sample(exercises, min(k, len(exercises)))