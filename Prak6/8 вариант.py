from random import randint

print('Вариант 8')
print('Задание 1')
n = int(input('Кол-во элементов в массиве: '))
d = []
for i in range(n):
    d.append(randint(1, 10))
print(d)
summa = 0
proiz = 1
for i in range(len(d)):
    summa += d[i]
    proiz *= d[i]
print(summa, proiz)
#1. Найдите сумму и произведение элементов списка. Результаты вывести на
#экран.

print('Задание 2')
m1 = int(input('Кол-во элементов в массиве: '))
n1 = []
for i in range(m1):
    n1.append(int(input('Элементы массива: ')))
sr = sum(n1)/len(n1)
for i in range(len(n1)):
    if n1[i] == 0:
        n1[i] = sr
print(n1)

#2. В массиве действительных чисел все нулевые элементы заменить на среднее
#арифметическое всех элементов массива