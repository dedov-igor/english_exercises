from gensim import downloader

from english_exercises.exercise.auxiliary_verb import create_auxiliary_verb_exercises
from english_exercises.exercise.sentence_transformation import create_sentence_transformation
from english_exercises.exercise.verb_form import choose_correct_verb_form
from english_exercises.exercise.words_by_association import words_by_association
from english_exercises.util import selection_of_k_exercises


def create_exercises_dataset(sentences):
    model = downloader.load("glove-wiki-gigaword-100")
    exercises = []
    exercises.extend(selection_of_k_exercises(create_auxiliary_verb_exercises(sentences)))
    exercises.extend(selection_of_k_exercises(choose_correct_verb_form(sentences)))
    exercises.extend(selection_of_k_exercises(words_by_association(sentences, model)))
    exercises.extend(selection_of_k_exercises(create_sentence_transformation(sentences, model)))
    return exercises