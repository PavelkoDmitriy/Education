class WordsFinder:
    
    def __init__(self, *file_names):
        self.list_ = file_names
        self.dict_ = {}

    def get_all_words(self):
        
        chars_ = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.list_:
            with open(i, "r", encoding="utf-8") as file:
                text = file.read()
                for char in chars_:
                    text = text.replace(char, '')
                self.dict_[i] = text.split()
        return self.dict_
    def find(self, word):
        result = {}
        flag = 1
        for key_ in self.dict_:
            for word_ in self.dict_[key_]:
                if word_.lower() == word.lower():
                    result[key_] = flag
                    break
                flag += 1
            flag = 1    
        return result

    def count(self, word):
        result = {}
        for key_ in self.dict_:
            flag = 0
            for word_ in self.dict_[key_]:
                if word_.lower() == word.lower():
                    flag += 1
            result[key_] = flag
        return result




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('text')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего"""

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
