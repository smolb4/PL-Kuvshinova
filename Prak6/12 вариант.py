from random import randint

print('Вариант 12')
print('Задание 1')
n = randint(1, 10)
d = []
for i in range(n):
    d.append(randint(1, 10))
print(d)
a = []
for i in range(len(d)):
    if d[i]%2==1:
        a.append(d[i])
if len(a)==0:
    print('Нет нужных значений')
else:
    print(min(a))

#1. Найти наименьший нечетный элемент списка и вывести его на экран

print('Задание 2')
m1 = 10
a = []
b = []
for i in range(m1):
    a.append(randint(1, 10))
    b.append(randint(1, 10))
a, b = b, a
print('Массив А: ', a, 'Массив В: ', b)


#2. Даны массивы A и B одинакового размера 10. Поменять местами их
#содержимое и вывести вначале элементы преобразованного массива A, а затем
#— элементы преобразованного массива B.