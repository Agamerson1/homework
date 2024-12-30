import time
import threading


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8'):
        for i in range(word_count):
            print(f'Какое-то слово № {i + 1}')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


time_start = time.time()
thread = threading.Thread(target=wite_words)
thread.start()
thread.join()
