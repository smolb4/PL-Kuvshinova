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
n=int(input('Строчки: ')) #строчки
m=int(input('Столбцы: ')) #столбцы
for i in range(n):
    b=[]
    for j in range(m):
        b.append(randint(1,100))
    a.append(b)
for i in a:
    print(i)


max1=0
min1=100
for i in a:
    min1=i.index(min(i))
    max1=i.index(max(i))
    i[max1],i[0]=i[0],i[max1]
    i[min1],i[-1]=i[-1],i[min1] # обмен 2-ух переменных через временный кортеж

print('Измененный массив:')
for i in a:
    print(i)

#2. Дана матрица B[N, М]. Найти в каждой строке матрицы
#максимальный и минимальный элементы и поменять их с первым и
#последним элементами строки соответственно.
