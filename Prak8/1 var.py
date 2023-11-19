print ('Вариант 1')
print ('Задание 1')

a=[]
n=int(input('Введите размер квадрата: '))
for i in range(n):
    b=[]
    for i in range(n):
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
