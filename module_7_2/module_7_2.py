def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding="utf-8")
    dict_ = {}
    flag = 1
    for i in strings:
        dict_[(flag, file.tell())] = i
        file.write(f"{i}\n")
        flag += 1
    file.close()
    return dict_


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)