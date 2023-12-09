from random import randint

print('Вариант 14')
print('Задание 1')
n = randint(3, 5)
d = []
for i in range(n):
    d.append(randint(10, 50))
print(d)
max1 = max(d)
min1 = min(d)
for i in range(len(d)):
    if d[i] == max1:
        d[i] = min1
    elif d[i] == min1:
        d[i] = max1
print(d)

#1. Найти максимальный элемент численного массива и поменять его местами с
#минимальным.

print('Задание 2')
m1 = 10
a = []
for i in range(m1):
    a.append(int(input()))
print('Исходный массив: ', a)
sred = sum(a)/len(a)
print('Среднее ариметическое: ', sred)
for i in range(len(a)):
    if a[i]>sred:
        a[i] = 1
print('Измененный массив: ', a)
#2. Программа заполняет одномерный массив из 10 целых чисел числами,
#считанными с клавиатуры. Определить среднее арифметическое всех чисел
#массива. Заменить элементы массива большие среднего арифметического на 1