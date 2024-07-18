# "Слишком древний шифр"

# import random
#
# n = random.randint(3, 20)
# print(f'{n} - ', end='')
# for i in range(1, n):
#     for j in range(i, n):
#         if n % (i + j) == 0 and i != j:
#             print(f'{i}{j}', end='')

n = int(input('Введите число от 3 до 20: '))


def game_of_life():
    num1 = n
    list_1 = []
    for i in range(1, n):
        for j in range(i, n):
            if num1 % (i + j) == 0 and i != j:
                list_2 = [i, j]
                list_1.append(list_2)

    return list_1


result = game_of_life()
result = str(result)
result = result.replace("[", "")
result = result.replace("]", "")
result = result.replace(",", "")
result = result.replace(" ", "")
print(f'{n} - {result}')