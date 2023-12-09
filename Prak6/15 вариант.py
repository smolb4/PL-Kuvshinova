from random import randint

print('Вариант 15')
print('Задание 1')
n = randint(4, 10)
d = []
for i in range(n):
    d.append(randint(1, 10))
print(d)
povtor = []
for i in d:
    if d.count(i) > 1 and i not in povtor:
        povtor.append(i)
    else:
        pass
if len(povtor) == 0:
    print('Повторяющиеся элементы в списке отсутствуют')
else:
    print(povtor)
#1. Определите, есть ли в списке повторяющиеся элементы, если да, то вывести
#на экран эти значения.

print('Задание 2')
m1 = randint(4, 10)
a = []
b = []
for i in range(m1):
    a.append(randint(4, 10))
print('Исходный массив: ', a)
for i in range(len(a)):
    if a[i]%2==1:
        b.append(a[i])
    else:
        pass
if len(b) == 0:
    print('В массиве нет нечетных чисел')
else:
    b.sort(reverse=True)
    print('Измененный массив: ', b)
#2. Дан одномерный массив целого типа. Получить другой массив, состоящий
#только из нечетных чисел исходного массива или сообщить, что таких чисел нет.
#Полученный массив вывести в порядке убывания элементов.