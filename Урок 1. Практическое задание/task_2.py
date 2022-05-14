"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

def first(arr, min_num=None):
    """
    Рекуссия O(n^2), или как как придумать проблемму из ничего)
    :param arr:
    :param min_num:
    :return:
    """
    if min_num is None:
        min_num = arr.pop()
    current = arr.pop()
    if current < min_num:
        min_num = current
    if arr:
        return first(arr, min_num)
    return min_num



def second(user_list):
    """
    Сложность этого алгоритма O(2n) (O(n) - на переборку и столько же на range(len(user_list)))
    :param user_list:
    :return:
    """
    min_num = user_list[0]
    for i in range(len(user_list)):
        if user_list[i] < min_num:
            min_num = user_list[i]
    return min_num


list_1 = [10, 0, 2, 56, 3, -5, -78]
list_2 = [10, 0, 2, 56, 3, -5, -78]

print('Работа первой функции -> ', first(list_1))
print('Работа второй функции -> ', second(list_2))