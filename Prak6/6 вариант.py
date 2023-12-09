from random import randint

print('Вариант 6')
print('Задание 1')
n = 10
d = []
for i in range(n):
    d.append(randint(10, 50))
k_bol = 0
k_men = 0
print(d)
for i in range(len(d)):
    if d[i] > d[-1]:
        k_bol += 1
    else:
        k_men += 1
print(k_bol, k_men)
#1. Дан одномерный массив из 10 целых чисел. Найти максимальный элемент и
#сравнить с ним остальные элементы. Вывести количество меньших
#максимального и больших максимального элемента.

print('Задание 2')
m1 = 10
n = []
for i in range(m1):
    n.append(int(input('Элементы массива: ')))
print(n)
s = 0
for i in range(len(n)):
    if n[i]>5:
        s += n[i]
print(s)

#2. Одномерный массив из 10-и целых чисел заполнить с клавиатуры,
#определить сумму тех чисел, которые >5.