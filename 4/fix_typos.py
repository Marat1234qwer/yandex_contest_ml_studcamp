"""
Читаем данные.
Сортируем словарь по длинне слов.
Для проверки слов используем коэффициент Левенштейна, если ошибок
нет - добавляем '0'. Если 1 ошибка - '1' и правильное слово.
Оставшимся словам добавляем '3+'
Записываем ответ в файл.
!!! Не написан алгоритм для проверки на ввод большего или меньшего
количества букв.
Не написан алгоритм проверки на 2 ошибки. !!!
"""
import Levenshtein


def read_data() -> tuple[list[str], list[str]]:
    with open('dict.txt', 'r') as dict:
        lst_dict = dict.readlines()
    with open('queries.txt', 'r') as queries:
        lst_queries = queries.readlines()
    return lst_dict, lst_queries


def sorted_dict(lst_dict) -> list:  # создаем список в котором слова из словаря находятся в разных списках, рассортированых по длинне слова
    lst_dict_sort = []
    for i in range(20):
        lst_insert = []
        lst_dict_sort.append(lst_insert)
    for i in range(len(lst_dict)):
        len_i = len(lst_dict[i])
        lst_dict_sort[len_i-6].append(lst_dict[i])
    return lst_dict_sort


def check_algorithm_0(lst_queries, lst_dict_sort) -> list:
    for i in range(len(lst_queries)):
        word = lst_queries[i]
        len_word = len(word) - 6
        for j in range(len(lst_dict_sort[len_word])):
            if word == lst_dict_sort[len_word][j]:
                lst_queries[i] = lst_queries[i].replace('\n', ' 0\n')
    return lst_queries


def check_algorithm_1(lst_queries_answer_0, lst_dict_sort) -> list:  # функция проверки на 1 ошибку
    try:
        for i in range(len(lst_queries_answer_0)):
            word = lst_queries_answer_0[i][0:-1]  # берем каждое слово на проверку, удаляем знак '\n'
            len_word = len(lst_queries_answer_0[i]) - 6
            for j in range(len(lst_dict_sort[len_word])):
                ratio = Levenshtein.ratio(word, lst_dict_sort[len_word][j][0:-1])  # коэффициент Левенштейна
                weight = ratio / (len(word) - 1) * len(lst_dict_sort[len_word][j][0:-1])  # считаем вес для одной буквы, затем умножаем на количество букв
                if weight == 1:  # если вес = 1, значит 1 ошибка
                    lst_queries_answer_0[i] = lst_queries_answer_0[i].replace('\n', f' 1 {lst_dict_sort[len_word][j]}')
                    break
    except Exception as ex:
        print(ex)
    finally:
        return lst_queries_answer_0


def check_algorithm_3(lst_queries_answer_1) -> list:
    for i in range(len(lst_queries_answer_1)):
        if lst_queries_answer_1[i].count('0') or lst_queries_answer_1[i].count('1'):
            continue
        else:
            lst_queries_answer_1[i] = lst_queries_answer_1[i].replace('\n', ' 3+\n')
    return lst_queries_answer_1


def write_data(lst_queries_answer_3):
    with open('answer.txt', 'w') as answer:
        answer.writelines(lst_queries_answer_3)


def main():
    lst_dict, lst_queries = read_data()
    lst_dict_sort = sorted_dict(lst_dict)
    lst_queries_answer_0 = check_algorithm_0(lst_queries, lst_dict_sort)
    lst_queries_answer_1 = check_algorithm_1(lst_queries_answer_0, lst_dict_sort)
    lst_queries_answer_3 = check_algorithm_3(lst_queries_answer_1)
    write_data(lst_queries_answer_3)


if __name__ == '__main__':
    main()
