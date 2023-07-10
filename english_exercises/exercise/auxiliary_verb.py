# Создание упражнений: вставка вспомогательного глагола
import logging

from spacy.tokens import Span

from english_exercises.exercise.exercise import Exercise
from english_exercises.util import replace_word

AUXILIARY_VERBS = ['am', 'are', 'is', 'was', 'were', 'do', 'does', 'did', 'have', 'has', 'had', 'doing', 'having',
                 'should', 'will']
DESCRIPTION = 'Заполните пропуск вспомогательным глаголом'


def create_auxiliary_verb_exercises(sentences: list[Span]):
    exercise_auxiliary_verb = []

    for s in sentences:
        for token in s:
            if token.text in AUXILIARY_VERBS:
                exercise_auxiliary_verb.append(
                    Exercise(s.text, 'missing_word', replace_word(s.text, token, s.start_char),[], {token.text}, DESCRIPTION)
                )

                break
    logging.info(f'Количество созданных упражнений {len(exercise_auxiliary_verb)}')
    return exercise_auxiliary_verb