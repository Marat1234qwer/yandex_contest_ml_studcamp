"""
Считываем данные.
Находим подходящие названия университетов с помощью difflib.
Записываем данные в файл answer.txt
"""
import difflib


def read_data() -> tuple[list[str], list[str]]:
    with open('universities.txt', 'r') as universities:
        lst_universities = universities.readlines()
    with open('queries.txt', 'r') as queries:
        lst_queries = queries.readlines()
    return lst_universities, lst_queries


def search_matches_name(lst_universities, lst_queries) -> list:
    lst_queries_answer = []
    for i in range(len(lst_queries)):  # поиск наиболее подходящего названия
        matches_name = difflib.get_close_matches(lst_queries[i], lst_universities, n=1)
        if matches_name == []:  # если название не найдено, переходим на следующую строку
            matches_name = '\n'
            lst_queries_answer.append(matches_name)
        else:
            lst_queries_answer.append(matches_name)
    lst_answer = []  # заносим названия в один список
    for i in range(len(lst_queries_answer)):
        lst_answer.append(lst_queries_answer[i][0])
    return lst_answer


def write_answer(lst_answer):
    with open('answer.txt', 'w') as answer:
        answer.writelines(lst_answer)


def main():
    lst_universities, lst_queries = read_data()
    lst_answer = search_matches_name(lst_universities, lst_queries)
    write_answer(lst_answer)


if __name__ == '__main__':
    main()
