import random

import numpy as np
from spacy.tokens import Span

from english_exercises.exercise.exercise import Exercise
from english_exercises.util import replace_word

POS_TAGS = ['NOUN', 'VERB', 'ADV', 'ADJ']

DESCRIPTION = 'Выберите правильное предложение'

def create_synonym(model, top_words_count, token):
    m = random.randint(0, top_words_count)
    synonym = model.most_similar(token.text.lower(), topn=top_words_count)[m][0]
    synonym = synonym.title() if token.text.istitle() else synonym
    return synonym

def create_antonym(model, top_words_count, token):
    m = random.randint(0, top_words_count)
    antonym = model.most_similar(positive=[token.text.lower(), 'bad'], negative=['good'],
                                 topn=top_words_count)[m][0]
    antonym = antonym.title() if token.text.istitle() else antonym
    return antonym

def create_sentence_transformation(sentences: list[Span], model, top_words_count = 5):
    # Упражнение: выбрать правильное предложение
    exercise_sentence_transf = []
    for s in sentences:
        if len(s) > 40:  # трансформацию не будем делать на коротких предложениях
            for token in s:
                if token.pos_ in POS_TAGS:
                    synonym = create_synonym(model, top_words_count, token)
                    antonym = create_antonym(model, top_words_count, token)


                    new_sent_1 = replace_word(s.text, token, s.start_char, synonym)
                    new_sent_2 = replace_word(s.text, token, s.start_char, antonym)
                    options = [s, new_sent_1, new_sent_2]
                    random.shuffle(options)

                    exercise_sentence_transf.append(
                        Exercise(s.text, 'select_word', '',
                                 options, {s.text}, DESCRIPTION)
                    )

                    break
    print(f'Количество созданных упражнений {len(exercise_sentence_transf)}')
    return exercise_sentence_transf