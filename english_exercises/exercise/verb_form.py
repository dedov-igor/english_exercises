# Создание упражнений: выбрать правильную форму глагола
import logging

from spacy.tokens import Span

from english_exercises.exercise.exercise import Exercise
from english_exercises.util import replace_word

INFLECTIONS = ['VB', 'VBP', 'VBZ', 'VBG', 'VBD']

DESCRIPTION = 'Выберите слово'

def choose_correct_verb_form(sentences: list[Span]):
    exercise_correct_verb_form = []
    for s in sentences:
        for token in s:
            if token.pos_ == 'VERB':
                options = {token._.inflect(form) for form in INFLECTIONS}
                options.add(token.text)
                exercise_correct_verb_form.append(Exercise(
                    s.text, 'select_word', replace_word(s.text, token, s.start_char),
                    list(options), {token.text}, DESCRIPTION
                ))
                break

    logging.info(f'Количество созданных упражнений {len(exercise_correct_verb_form)}')
    return exercise_correct_verb_form