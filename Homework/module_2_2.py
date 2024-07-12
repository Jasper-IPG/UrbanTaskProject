# Задача "Все ли равны?"
first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))
if first == second and first == third and second == third:
    print(3)
# elif (first == second and not first == third
#      or first == third and not first == second
#      or second == third and not second == first):
elif first == second != third or first == third != second or second == third != first:
    print(2)
elif first != second and first != third and second != third:
    print(0)
else:
    print('Что-то пошло не так...')
