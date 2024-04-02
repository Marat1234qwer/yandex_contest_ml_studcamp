"""
Считываем данные. Переворачиваем список.
Представим диаграмму в виде матрицы, в каждую клетку будем вносить
числа - длинна крюка который можно начать с этой строки.
Затем считаем количество крюков, длину которого вносили при запросе.
"""
n, k = map(int, input().split())
lst_data = []
for i in range(n):
    s = int(input())
    lst_data.append(s)

lst_data.reverse()  # переворачиваем список
lst_crook = []  # матрица длин крюков
lst_insert_0 = []  # заполняем первую строку матрицы
g = 1
while g <= lst_data[0]:
    lst_insert_0.append(g)
    g += 1
lst_crook.append(lst_insert_0)

f = 1  # заполняем оставшуюся матрицу числами(длина крюка)
while f < len(lst_data):
    lst_insert = [0] * lst_data[f]
    lst_insert[0] = 1
    dif = lst_data[f] - lst_data[f-1]
    for i in range(dif-1):
        lst_insert[i+1] = i + 2
    for j in range(lst_data[f]-dif):
        lst_insert[j+dif] = dif + 1 + lst_crook[f-1][j]
    lst_crook.append(lst_insert)
    f += 1

count = 0  # считаем количество крюков, длину которого запросили
for i in range(len(lst_data)):
    if lst_crook[i].count(k):
        count += 1
print(count)
