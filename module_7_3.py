class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    elem = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for i in elem:
                        line = line.replace(i, '')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        for value, key in self.get_all_words().items():
            if word.lower() in key:
                result[value] = key.index(word.lower()) + 1
        return result


    def count(self, word):
        result2 = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            result2[file_name] = words.count(word)
        return result2


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))





















































