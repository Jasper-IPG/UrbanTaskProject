# "Многопроцессное считывание"
import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='UTF8') as file:
        while True:
            data = file.readline()
            all_data.append(data)
            if not data:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
# time_start = datetime.now()
# for item in filenames:
#     read_info(item)
# time_end = datetime.now()
# time_res = time_end - time_start
# print(f'Линейный вызов функции: {time_res}')

# Многопроцессный
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        time_start = datetime.now()
        pool.map(read_info, filenames)
        time_end = datetime.now()
        time_res = time_end - time_start
        print(f'Многопроцессный вызов функции: {time_res}')
