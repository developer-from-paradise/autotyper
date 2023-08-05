import pyautogui as p
from time import sleep

# Ask the user for the number of rows (how many words to type)
rows = int(input('Введите кол. строк: '))

# Define a mapping for Cyrillic to Latin characters
layout = dict(zip(map(ord, "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                           'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'),
                           "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                           'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'))

# Initialize lists to store words and columns
words = []
columns = []

# Ask the user if the word changes for each row
is_changes = input('Слово меняется? [Да | Нет]: ')

# Depending on the user's response, collect words for each row accordingly
if 'да' in is_changes:
    for i in range(0, rows):
        words.append(input('Введите слово: ').translate(layout))
else:
    word = input('Введите слово: ').translate(layout)
    for i in range(0, rows):
        words.append(word)

# Ask the user if the number of inputs changes for each row
is_changes_2 = input('Количество вводов меняется? [Да | Нет]: ')

# Depending on the user's response, collect the number of inputs for each row accordingly
if 'да' in is_changes_2:
    for i in range(0, rows):
        columns.append(int(input('Введите кол. вводов: ')))
else:
    row_words = int(input('Введите кол. вводов: '))
    for i in range(0, rows):
        columns.append(row_words)

# Start a countdown before executing the typing
for i in range(0, 5):
    print(f'Запуск через...{i+1}')
    sleep(1)


print('Работаю...')
# Typing process: iterate through each row and type the words specified for each row
for l in range(0, rows):
    symbols = list(words[l])
    for i in range(0, columns[l]):
        for word in symbols:
            p.press(word)

# Notify that the typing is completed
print('Готово!')