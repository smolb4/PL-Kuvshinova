from random import randint

print('Вариант 7')
print('Задание 1')
n = int(input('Кол-во элементов в массиве: '))
d = []
for i in range(n):
    d.append(randint(1, 10))
print(d)
summa = 0
proiz = 1
for i in range(len(d)):
    if i%2==0:
        summa += d[i]
    else:
        proiz *= d[i]
print(summa, proiz)
#1. Дан массив целых чисел. Найти сумму элементов с четными номерами и
#произведение элементов с нечетными номерами. Вывести сумму и
#произведение.

print('Задание 2')
m1 = int(input('Кол-во элементов в массиве: '))
n = []
for i in range(m1):
    n.append(randint(1, 10))
print(n)
a = n.index(max(n))
b = n.index(min(n))

n[a], n[b] = n[b], n[a]
print(n)

#2. Переставить в одномерном массиве минимальный элемент и максимальный
