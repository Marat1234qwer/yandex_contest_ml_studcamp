"""
from collections import Counter


n = int(input())
print(Counter(list(map(int, input().split()))).most_common()[0][0])

Собственная реализация Counter
"""


class Mcounter:

    def __init__(self, lst) -> None:
        self.lst = lst

    def m_most_common(self) -> list:  # метод принимает список, возвращает список - число и количество чисел в списке
        lst_num = [0]  # создаем два списка. Один с числами, другой с количеством чисел
        lst_num[0] = self.lst[0]
        lst_amount = [1]
        j = 0
        for i in range(1, len(self.lst)):
            if self.lst[i] == lst_num[j]:
                lst_amount[j] += 1
            else:
                lst_num.append(self.lst[i])
                lst_amount.append(1)
                j += 1
        lst_merge = []  # список mos_common
        for i in range(len(lst_num)):
            tpl = (lst_num[i], lst_amount[i])
            lst_merge.append(tpl)
        return lst_merge

    def __str__(self) -> str:
        return f'{self.lst}'


def main():
    n = int(input())
    lst_m = list(map(int, input().split()))
    lst_m.sort(reverse=True)
    print(Mcounter(lst_m).m_most_common()[0][0])


if __name__ == '__main__':
    main()
