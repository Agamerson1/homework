word = 'text'


class WordsFinder:
    def __init__(self, *names):
        self.file_names = list(names)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                file_words = []
                for line in file:
                    chars = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    words = line.lower()
                    for char in chars:
                        words = words.replace(char, '')
                    words = words.split()
                    file_words.extend(words)
            all_words[name] = file_words
            return all_words

    def find(self, word):
        find_words = {}
        for names, words in self.get_all_words().items():
            if word in words:
                finder = words.index(word.lower())
                find_words[names] = finder
        return find_words

    def count(self, word):
        count_words = {}
        for names, words in self.get_all_words().items():
            if word in words:
                counter = words.count(word.lower())
                count_words[names] = counter
        return count_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('text'))  # 3 слово по счёту
print(finder2.count('text'))  # 4 слова teXT в тексте всего
