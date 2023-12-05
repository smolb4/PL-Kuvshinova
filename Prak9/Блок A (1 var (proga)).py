print ('Блок А')
print ('Задание 1')
def f (a):
    if a==1:
        return 1
    else:
        return a*f(a-1) #факториал
x = int(input('x: '))
n = int(input('n: '))
b = (x**n)/f(n)
print('Ответ: ', b)

#1.Даны натуральные числа Х, N.
#Вычислить выражение вида: x ^ n / n!.
