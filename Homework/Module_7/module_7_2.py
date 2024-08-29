# "Записать и запомнить"
def custom_write(file_name, strings):
    strings_positions = {}
    key_list = []
    value_list = []
    for item in strings:
        value_list.append(item)
        file = open(file_name, 'a', encoding='UTF-8')
        key_list.append(file.tell())
        file.write(f'{item}\n')
        file.close()
        strings_positions = dict(zip(enumerate(key_list, 1), value_list))
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
