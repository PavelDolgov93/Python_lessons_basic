
__author__ = 'Долгов Павел Григорьевич'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

chislo = 1234

while chislo % 10 != 0:
    print(chislo % 10)
    chislo = chislo // 10


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

print('')

# В задании не указан тип переменных, поэтому решил через дополнительную переменную

perem1 = input('perem1 = ')
perem2 = input('perem2 = ')

perem_cash = perem1
perem1 = perem2
perem2 = perem_cash

print('perem1 = ', perem1)
print('perem2 = ', perem2)

# Решение через арифметические действия для чисел:

perem1 = int(input('perem1 (число) = '))
perem2 = int(input('perem2 (число) = '))

perem1 = perem1 + perem2
perem2 = perem1 - perem2
perem1 = perem1 - perem2

print('perem1 = ', perem1)
print('perem2 = ', perem2)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

print('')

vozr = input('Введите возраст: ')

if int(vozr) >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')
