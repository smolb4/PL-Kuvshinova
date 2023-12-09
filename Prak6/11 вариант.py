from random import randint

print('Вариант 11')
print('Задание 1')
n = randint(4, 10)
d = []
for i in range(n):
    d.append(randint(1, 10))
print(d)
a = []
for i in range(len(d)):
    if d[i]%2==0:
        a.append(d[i])
print(max(a))
#1 Найти наибольший элемент списка, который делиться на 2 без остатка и
#вывести его на экран.

print('Задание 2')
m1 = randint(4, 10)
a = []
b = []
for i in range(m1):
    a.append(randint(1, 30))
print('Массив А: ', a)
for i in range(len(a)):
    if a[i]%2==0 and a[i]<10:
        b.append(a[i])
    else:
        pass
if len(b) == 0:
    print('Четных чисел меньше 10 нет')
else:
    print('Полученный массив: ', sorted(b))


#2. Дан одномерный массив целого типа. Получить другой массив, состоящий
#только из четных чисел исходного массива, меньше 10, или сообщить, что таких
#чисел нет. Полученный массив вывести в порядке возрастания элементов