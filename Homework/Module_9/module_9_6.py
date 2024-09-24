# "Генераторы"
def all_variants(text):
    for elem in range(len(text)):
        for elem_ in range(len(text) - elem):
            yield text[elem_: elem + elem_ + 1]


a = all_variants("abc")
for i in a:
    print(i)

"""
Вывод на консоль:
a
b
c
ab
bc
abc
"""
