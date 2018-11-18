
__author__ = 'Долгов Павел Григорьевич'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

spisok_fruktov = ["яблоко", "банан", "киви", "арбуз"]

max_simvolov = 0

for frukt in spisok_fruktov:
    kolvo_simvolov = len(frukt)
    if kolvo_simvolov > max_simvolov:
        max_simvolov = kolvo_simvolov

nom =1
for frukt in spisok_fruktov:
    format_stroka = str(nom)+'. {:>'+str(max_simvolov)+'}'
    print(format_stroka.format(frukt))
    nom = nom + 1


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print('')

spisok1 = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
spisok2 = [3, 4, 'a', 'b']

mnozhestvo1 = set(spisok1)
mnozhestvo2 = set(spisok2)

obshee = mnozhestvo1.intersection(mnozhestvo2)

for znch in obshee:
    spisok1.remove(znch)

print(spisok1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print('')

s = [1, 3, 23, 32, 78, 2, 36, 55]
s_new = []

for elem in s:
    if elem%2 == 0:
        s_new.append(elem / 4)
    else:
        s_new.append(elem * 2)

print(s_new)