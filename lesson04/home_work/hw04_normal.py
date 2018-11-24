
__author__ = 'Долгов Павел Григорьевич'

# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
# import random

from random import randint

f = open('C:\\Users\\Public\dz.txt', 'w', encoding='utf-8')
for i in range(2500):
    f.write(str(randint(0,9)))
f.close()

f = open('C:\\Users\\Public\dz.txt', 'r')
s = list(f.read())
f.close()

first = True

for elem in s:

    if first:
        first = False

        count_max = 1
        count_curr = 1
        cif_max = elem
        cif_curr = elem

    else:
        if cif_curr == elem:
            count_curr = count_curr + 1

            if count_curr > count_max:
                count_max = count_curr
                cif_max = cif_curr

        else:
            cif_curr = elem
            count_curr = 1

for i in range(count_max):
    print(cif_max, end='')


# Задание-2
# Сформировать квадратную матрицу, в каждой строке которой находится ровно один ноль на случайном месте,
# остальные элементы тоже рандомные. Пользователь вводит размер

print('')

size = int(input('Размер матрицы:'))

matr = [ [ randint(1,9) for col in range(size)] for row in range(size) ]

for row in range(size):
    matr[row][randint(0, size-1)] = 0

    print(matr[row])

