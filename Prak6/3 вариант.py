from random import randint

print('Вариант 3')
print('Задание 1')
n = int(input('Кол-во элементов в массиве: '))
d = []
for i in range(n):
    d.append(randint(0, 10))
s = 0
for i in range(len(d)):
    if i % 2 == 1:
        s = s + d[i]
print(f'Массив: {d}, Сумма: {s}')

#1. В одномерном числовом массиве D длиной n вычислить сумму элементов с
#нечетными индексами. Вывести на экран массив D, полученную сумму.

print('Задание 2')
m1 = 8
n = []
for i in range(m1):
    n.append(randint(0, 30))
print('Исходный массив: ', n)
for i in range(len(n)):
    if n[i] < 15:
        n[i] = n[i] * 2
print('Преобразованный массив: ', n)
#2. Дан одномерный массив из 8 элементов. Заменить все элементы массива
#меньшие 15 их удвоенными значениями. Вывести на экран монитора
#преобразованный массив.