from random import randint

print('Вариант 13')
print('Задание 1')
n = 10
d = []
for i in range(n):
    d.append(randint(-50, 50))
print(d)
for i in range(len(d)):
    if d[i-1]<0 and d[i]<0:
        print(d[i-1], d[i])

#1. Дан одномерный массив из 10 целых чисел. Вывести пары отрицательных
#чисел, стоящих рядом

print('Задание 2')
m1 = 8
a = []
b = []
for i in range(m1):
    a.append(randint(1, 30))
print('Исходный массив: ', a)
for i in range(len(a)):
    if a[i] < 15:
        a[i] *= 2
print(a)
#2. Дан одномерный массив из 8 элементов. Заменить все элементы массива
#меньшие 15 их удвоенными значениями. Вывести на экран монитора
#преобразованный массив.