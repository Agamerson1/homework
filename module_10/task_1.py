import time
import threading


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8'):
        for i in range(word_count):
            i += 1
            print(f'Какое-то слово № {i}')
