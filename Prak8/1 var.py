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

a=[]
n=3
m=4
for i in range(n):
    b=[]
    for j in range(m):
        b.append(int(input('Введите элементы матрицы: ')))
    a.append(b)
for i in a:
    print(i)

maximum=a[0][0]
minimum=a[0][-1]
for i in range(n):
    for j in range(m):
        if maximum<a[0][j]:

            maximum=a[0][j]
            a[0][0], a[0][j] = a[0][j], a[0][0]

        if minimum>a[0][j]:
            minimum=a[0][j]
            a[0][-1], a[0][j] = a[0][j], a[0][-1]

maximum=a[1][0]
minimum=a[1][-1]
for i in range(n):
    for j in range(m):
        if maximum<a[1][j]:
            maximum=a[1][j]
            a[1][0], a[1][j] = a[1][j], a[1][0]
        if minimum>a[1][j]:
            minimum=a[1][j]
            a[1][-1], a[1][j] = a[1][j], a[1][-1]


maximum=a[2][0]
minimum=a[2][-1]
for i in range(n):
    for j in range(m):
        if maximum<a[2][j]:
            maximum=a[2][j]
            a[2][0], a[2][j] = a[2][j], a[2][0]
        if minimum>a[2][j]:
            minimum=a[2][j]
            a[2][-1], a[2][j] = a[2][j], a[2][-1]

print('Измененный массив:')
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()

#2. Дана матрица B[N, М]. Найти в каждой строке матрицы
#максимальный и минимальный элементы и поменять их с первым и
#последним элементами строки соответственно.
