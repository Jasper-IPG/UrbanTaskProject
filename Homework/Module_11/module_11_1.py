# "Сторонние библиотеки Python"
import requests
import numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageFont

'''
Requests — это библиотека, которая создана для быстрой и простой работы с запросами.
Коды состояний имеют вид трёхзначных чисел от 100 до 500. 
Наиболее известные коды:
200 — "OK". Запрос прошёл успешно и получен ответ.
400 — "Bad Request". Неправильный, некорректный запрос.
401 — "Unauthorized". Неавторизованный запрос.
403 — "Forbidden". Сервер понял запрос, но не может его выполнить. Недостаточно прав.
404 - "Not Found". Страница не найдена
'''
requests.get('https://kinopoisk.ru')  # Запрос.
answer = requests.get('https://kinopoisk.ru')  # Переменная, в которую хранится код состояния запрашиваемой страницы.
print('Библиотека Requests')
print(f'kinopoisk.ru - {answer}')  # Вывод кода состояния.
print()

'''
NumPy (расшифровывается как Numerical Python) — это библиотека для Python, которая позволяет работать с 
многомерными массивами и матрицами. Она подходит для научных и математических расчётов, поскольку отличается 
быстротой и эффективностью.
Некоторые области использования NumPy:
— Научные вычисления.
— Data Science.
— Machine Learning.
— Визуализация данных.
'''
numbers = [4, 8, 15, 16, 23, 42]

num = np.array(numbers)
mean_num = np.mean(numbers)
min_num = np.min(numbers)
max_num = np.max(numbers)
sum_num = np.sum(numbers)
prod_num = np.prod(numbers)
print('Библиотека NumPy')
print(numbers)
print(f'Минимальное число: {min_num}')
print(f'Среднее значение: {mean_num}')
print(f'Максимальное число: {max_num}')
print(f'Сумма чисел: {sum_num}')
print(f'Произведение чисел: {prod_num}')
print()

'''
Pillow — это бесплатная библиотека с открытым исходным кодом для работы с изображениями и их обработки на языке 
Python. Она является форком библиотеки Python Imaging Library (PIL).
Pillow поддерживает различные форматы файлов изображений, такие как .PNG, .JPEG, .PPM, .GIF, .TIFF и .BMP. С помощью 
этой библиотеки можно выполнять различные операции с изображениями, такие как обрезка, изменение размера, добавление 
текста, поворот, преобразование к оттенкам серого и многое другое. 
'''
img = Image.open('DeLorean.jpg')
print('Библиотека Pillow')
print(f'Размер изображения: {img.size}')
img.show()
new_size = (img.width // 2, img.height // 2)  # Уменьшаем размер изображения в два раза.
resized_img = img.resize(new_size)
resized_img.save('DeLorean_resized.png', format='PNG')  # Сохраняем преобразованное изображение в файл с форматом PNG.
resized_img.show()
print(f'Новый размер изображения: {resized_img.size}')
grayscale_img = img.convert('L')    # Преобразуем изображение в чёрно-белый формат
grayscale_img.save('DeLorean_grayscale.png', format='PNG')   # Сохраняем преобразованное изображение в файл с форматом PNG.
grayscale_img.show()
