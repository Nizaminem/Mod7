
import string

class WordsFinder:
    def _init_(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        # Перебираем каждый файл
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        content = content.replace(char, ' ')
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
                all_words[file_name] = []
        return all_words

    def find(self, word):
        """Находит первое вхождение слова в каждом файле."""
        word = word.lower()  # Переводим искомое слово в нижний регистр
        result = {}

        # Получаем словарь всех слов из файлов
        all_words = self.get_all_words()

        for name, words in all_words.items():
            try:
                # Найти индекс первого вхождения слова
                position = words.index(word) + 1  # Счёт начинается с 1
                result[name] = position
            except ValueError:
                # Если слово не найдено, пропускаем этот файл
                result[name] = None

        return result

    def count(self, word):
        """Считает количество вхождений слова в каждом файле."""
        word = word.lower()  # Переводим искомое слово в нижний регистр
        result = {}

        # Получаем словарь всех слов из файлов
        all_words = self.get_all_words()

        for name, words in all_words.items():
            # Считаем количество вхождений слова
            result[name] = words.count(word)

        return result


finder = WordsFinder('D:\\низаим\\PythonProjectForUrbanUniversityd\\Module7\\test_file.txt')

# Получить все слова из файлов
print(finder.get_all_words())

# Найти позицию первого вхождения слова
print(finder.find('TEXT'))

# Посчитать количество вхождений слова
print(finder.count('teXT'))