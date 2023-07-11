# Создание упражнений: подобрать ассоциации к слову
import contextlib
import logging

from spacy.tokens import Span, Token

from english_exercises.exercise.exercise import Exercise

from nltk.corpus import wordnet

def create_associations(model, token: Token):
    associations = set()
    associations.update(w[0] for w in model.similar_by_word(token.text))
    associations.update(w[0] for w in model.most_similar(positive=[token.text, 'good'], negative=['bad']))
    associations.update(w[0] for w in model.most_similar(positive=[token.text, 'man'], negative=['woman']))
    associations.update(w[0] for w in model.most_similar(positive=[token.text, 'short'], negative=['long']))
    return associations

def create_wordnet_associations(token: Token):
    associations = set()
    for e in wordnet.synsets(token.text):  # дополнительный поиск с помощью wordnet
        for syn in e.lemmas():
            associations.update([syn.name()])
            if syn.antonyms(): # check whether the antonyms for the given word are available or not
                associations.add(syn.antonyms()[0].name()) # антонимы тоже могут быть ассоциациями
    return associations

def delete_cognates(association_words_set, token: Token):
    del_words = set()
    for word in association_words_set:  # из списка ассоциаций удаляем однокоренные слова
        if word.find(token.text.lower()) != -1 or token.text.lower().find(word) != -1:
            del_words.add(word)
    return association_words_set - del_words


def words_by_association(sentences: list[Span], model):
    # Упражнение: подобрать ассоциации к слову
    exercise_association = []
    token_set = set()

    for s in sentences:
        for token in s:
            if token.pos_ in ['NOUN', 'VERB'] and not (token.text.istitle()) and len(token.text) > 4 and token.text not in token_set and token.text[-1] not in ['s', 'd']:
                # ассоциаций в списке должно быть много, чтобы не пришлось угадывать слово из небольшого списка
                association_words_set = create_wordnet_associations(token) | create_associations(model, token) # множество всех ассоциаций к слову
                association_words_set = delete_cognates(association_words_set, token)

                association_words_set = {w.replace('_', ' ') for w in association_words_set}

                if len(association_words_set) < 8:
                    continue  # Если ассоциаций мало не создаем упражнение на это слово

                exercise_association.append(
                    Exercise(s.text, 'missing_word', s.text,
                             [], association_words_set, f'Подберите ассоциацию к слову {token.text}')
                )
                token_set.add(token.text)

                break  # одно упражнение на одно предложение
    logging.info(f'Количество созданных упражнений {len(exercise_association)}')
    return exercise_association