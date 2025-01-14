from pprint import pprint

def custom_write(file_name, strings):
    string_positions = {}
    with open(file_name, 'w', encoding = 'utf-8') as file:
        for i, string in enumerate(strings, 1):
            position = file.tell()
            file.write(string + '\n')
            string_positions[(i, position)] = string
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
    
