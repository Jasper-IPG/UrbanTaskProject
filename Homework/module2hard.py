# "Слишком древний шифр"

import random

n = random.randint(3, 20)
print(f'{n} - ', end='')
for i in range(1, n):
    for j in range(i, n):
        if n % (i + j) == 0 and i != j:
            print(f'{i}{j}', end='')
