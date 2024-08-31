# "Найдёт везде"
class WordsFinder:
    file_names = []

    def __init__(self, *args):
        self.name = args
        self.file_names.extend(args)   # создать список из имён файлов

    def get_all_words(self):
        key_name = []
        value_word = []
        for j in self.file_names:                                         # создаем список ключей для словаря
            key_name.append(j)
            with open(j, encoding='UTF-8') as file:                       # просматриваем файлы, создаем список из слов
                words = file.read().lower().replace('\n', ' ')
                for k in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    words = words.replace(k, '')
                words = words.split()
                value_word.append(words)
        all_words = dict(zip(key_name, value_word))
        return all_words

    def find(self, word):
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                word_index = (words.index(word))
                return {name: word_index}

    def count(self, word):
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                word_count = (words.count(word))
                return {name: word_count}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту, его индекс в списке слов - 2
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
