import time
import threading
from threading import Thread


def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8'):
        for i in range(word_count):
            print(f'Какое-то слово № {i + 1}')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


time_start = time.time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_stop = time.time()

print(f'Время работы функции: {time_stop - time_start}')

time_start2 = time.time()
thread1 = Thread(target=wite_words, args=(10, 'example5.txt'))
thread2 = Thread(target=wite_words, args=(30, 'example6.txt'))
thread3 = Thread(target=wite_words, args=(200, 'example7.txt'))
thread4 = Thread(target=wite_words, args=(100, 'example8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

time_stop2 = time.time()
print(f'Время работы потоков: {time_stop2 - time_start2}')