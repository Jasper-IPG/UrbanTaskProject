# "Счётчик вызовов"

calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    string = (len(string), string.upper(), string.lower())
    return string


def is_contains(string, list_):
    count_calls()
    string = (string.lower())
    list_ = str(list_)
    list_ = (list_.lower())
    if string in list_:
        list_to_search = True
    else:
        list_to_search = False
    return list_to_search


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
