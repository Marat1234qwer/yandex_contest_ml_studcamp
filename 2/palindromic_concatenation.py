"""
Складываем две строки и сравниваем в получившийся строке
первый элемент с последним, затем второй элемент с
предпоследним, и так далее.
Если элементы в парах совпадают, то получившиеся строка палиндром - выводим
на печать номера строк которые складывали.
"""


def check(string, flag) -> bool:  # функция проверки слова на палиндром
    half_lenght = 0
    for i in range(len(string)//2):
        if string[i] == string[-1-i]:
            half_lenght += 1
        else:
            break
    if half_lenght == len(string) // 2:
        flag = True
    return flag


n = int(input())  # ввод даных
lst_strings = []
for i in range(n):
    s = input()
    lst_strings.append(s)

flag = False

for i in range(len(lst_strings)):
    for j in range(len(lst_strings)):
        if i != j:  # пропускаем если элемент суммирует сам себя
            string = lst_strings[i] + lst_strings[j]
            if check(string, flag):
                print(f'{i+1} {j+1}')
