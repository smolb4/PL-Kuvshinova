print ('Вариант 1')
print ('Задание 1')

a=[]
n=int(input('Введите размер квадрата: '))
for i in range(n):
    b=[]
    for j in range(n):
        b.append(int(input('Введите элементы матрицы: ')))
    a.append(b)
for i in a:
    print (i)

k=0
s=0
print ('Число и сумма')
for i in range(n):
    for j in range(n):
        if i<j and a[i][j]>0:
            k+=1
            s+=a[i][j]
print(k, s)

#1. Вычислить сумму и число положительных элементов матрицы A[N, N],
#находящихся над главной диагональю.

print ('Задание 2')
from random import randint
a=[]
n=3
m=4
for i in range(n):
    b=[]
    for j in range(m):
        b.append(randint(1,100))
    a.append(b)
for i in a:
    print(i)

maximum1=a[0][0]
minimum1=a[0][-1]
for i in range(n):
    for j in range(m):
        if maximum1<a[0][j]:
            maximum1=a[0][j]
            a[0][0], a[0][j] = a[0][j], a[0][0]

        if minimum1>a[0][j]:
            minimum1=a[0][j]
            a[0][j], a[0][-1] = a[0][-1], a[0][j]

maximum2=a[1][0]
minimum2=a[1][-1]
for i in range(n):
    for j in range(m):
        if maximum2<a[1][j]:
            maximum2=a[1][j]
            a[1][0], a[1][j] = a[1][j], a[1][0]
        if minimum2>a[1][j]:
            minimum2=a[1][j]
            a[1][j], a[1][-1] = a[1][-1], a[1][j]


maximum3=a[2][0]
minimum3=a[2][-1]
for i in range(n):
    for j in range(m):
        if maximum3<a[2][j]:
            maximum3=a[2][j]
            a[2][0], a[2][j] = a[2][j], a[2][0]
        if minimum3>a[2][j]:
            minimum3=a[2][j]
            a[2][j], a[2][-1] = a[2][-1], a[2][j]

print('Измененный массив:')
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()

#2. Дана матрица B[N, М]. Найти в каждой строке матрицы
#максимальный и минимальный элементы и поменять их с первым и
#последним элементами строки соответственно.
