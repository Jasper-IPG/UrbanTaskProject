# "Раз, два, три, четыре, пять .... Это не всё?"
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data):
    sum_ = 0
    for i in data:
        if isinstance(i, str):
            sum_ = sum_ + len(i)
        elif isinstance(i, int):
            sum_ = sum_ + i
        elif isinstance(i, dict):
            sum_ = (sum_ + sum(value for value in i.values() if isinstance(value, int)) +
                    sum(len(keys) for keys in i.keys() if isinstance(keys, str)))
        elif isinstance(i, (list, tuple, set)):
            sum_ = sum_ + calculate_structure_sum(i)
    return sum_


result = calculate_structure_sum(data_structure)
print(result)
