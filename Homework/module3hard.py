# "Раз, два, три, четыре, пять .... Это не всё?"
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum():
    sum_ = 0
    for i in data_structure:
        if isinstance(i, (list, int, float)):
            sum_ = sum_ + sum(i)
        elif isinstance(i, str):
            sum_ = sum_ + len(i)
        elif isinstance(i, dict):
            sum_ = (sum_ + sum(value for value in i.values() if isinstance(value, (int, float))) +
                    sum(len(keys) for keys in i.keys() if isinstance(keys, str)))
        elif isinstance(i, tuple):
            for j in i:
                if isinstance(j, int):
                    sum_ = sum_ + j
                elif isinstance(j, dict):
                    sum_ = (sum_ + sum(value for value in j.values() if isinstance(value, (int, float))) +
                            sum(len(key) for key in j.keys() if isinstance(key, str)))

    return sum_


result = calculate_structure_sum()
print(result)


