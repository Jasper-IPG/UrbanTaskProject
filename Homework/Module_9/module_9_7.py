# "Декораторы"
def is_prime(func):
    def wrapper(*args):
        func_res = func(*args)
        if func_res > 1:
            for i in range(2, func_res):
                if func_res % i == 0:
                    print('Составное')
                    break
            else:
                print('Простое')
        return func_res
    return wrapper


@is_prime
def sum_three(*args):
    sum_ = sum(args)
    return sum_


result = sum_three(2, 3, 6)
print(result)

"""
Вывод на консоль:
Простое
11
"""
