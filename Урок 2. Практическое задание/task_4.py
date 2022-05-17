"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def funny_sequence(n, next_el=1, sum_el=0):
    if n > 0:
        sum_el += next_el
        funny_sequence(n - 1, next_el * (-0.5), sum_el)
    else:
        return print(f' Результат работы программы : {sum_el}')


if __name__ == '__main__':
    a = int(input('Введите количество элементов n: '))
    funny_sequence(a)
