
__author__ = 'Долгов Павел Григорьевич'

# Задание-1
# Куб состоит из n^3 прозрачных и непрозрачных элементарных кубиков. Имеется ли хотя бы один просвет по каждому из трех измерений?
# Если это так, вывести координаты каждого просвета. Куб задается трехмерной матрицей из 0 и 1.

# Задание-2
# Дан pwd.txt с логинами и паролями. Найдите топ10 самых популярных паролей.

import re

f = open('C:\\Users\\Public\pwd.txt', 'r')
s = re.findall(r';.+', f.read())
f.close()

parol_kolvo = {}

for elem in s:
    if parol_kolvo.get(elem) == None:
        parol_kolvo[elem] = 1
    else:
        parol_kolvo[elem] = parol_kolvo[elem] + 1

paroli_sort = sorted(parol_kolvo.items(), key= lambda item: item[1], reverse=True)

for i in range(10):
    print(f'{i+1}. {paroli_sort[i][0][1:]} ({paroli_sort[i][1]})')


# Задание-3
# Пользователь вводит положительное целое число больше 1
# Нужно создать квадратную матрицу этого размера и по спирали заполнить её числами

# 5
#  1  2  3  4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

# 3
# 1 2 3
# 8 9 4
# 7 6 5

print('')


def poluchit_napravlenie(matr, x, y, size, napravlenie):

    # Возможен ли шаг

    if napravlenie == 'pravo':
        if (x + 1 <= size - 1 and matr[y][x + 1] == 0):
            pass
        else:
            napravlenie = 'vniz'

    if napravlenie == 'vniz':
        if (y + 1 <= size - 1 and matr[y + 1][x] == 0):
            pass
        else:
            napravlenie = 'vlevo'

    if napravlenie == 'vlevo':
        if (x - 1 >= 0 and matr[y][x - 1] == 0):
            pass
        else:
            napravlenie = 'vverh'

    if napravlenie == 'vverh':
        if (y - 1 >= 0 and matr[y - 1][x] == 0):
            pass
        else:
            napravlenie = 'pravo'

    return napravlenie


size = int(input('Размер матрицы:'))
matr = [ [0 for x in range(size)] for y in range(size) ]

x = 0
y = 0
napravlenie = 'pravo'

for cif in range(size*size):
    cif = cif + 1

    matr[y][x] = cif

    napravlenie = poluchit_napravlenie(matr, x, y, size, napravlenie)

    if napravlenie == 'pravo':
        x = x + 1
        continue

    if napravlenie == 'vniz':
        y = y + 1
        continue

    if napravlenie == 'vlevo':
        x = x - 1
        continue

    if napravlenie == 'vverh':
        y = y - 1
        continue

dlina = len(str(size*size))

for y in range(size):
    for x in range(size):
        print(f'{matr[y][x]:>{dlina}}', end= ', ')
    print('')