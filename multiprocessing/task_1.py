import multiprocessing
import time
from time import process_time


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    start_time = time.time()
    for name in filenames:
        read_info(name)
    line_time = time.time() - start_time
    print(f'Линейный вызов: {line_time} секунд')

    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    process_time = time.time() - start_time
    print(f'Многопроцессный вызов: {process_time} секунд')
