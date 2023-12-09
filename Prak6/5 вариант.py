from random import randint

print('Вариант 5')
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
m1 = 10
n = []
for i in range(m1):
    n.append(randint(10, 12))
print(n)
k = []
for i in range(len(n)):
    if n[i-1] != n[i]:
        k.append(n[i])
print(k)

#2. Дан целочисленный массив размера 10. Создать новый массив, удалив все
#одинаковые элементы, оставив их 1 раз.
