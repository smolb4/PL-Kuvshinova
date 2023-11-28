print ('Блок А')
print ('Задание 1')

import math
def vid(a,b):
    return (a**b)/math.factorial(b)


x = int(input())
n = int(input())

print(vid(x,n))
#1.Даны натуральные числа Х, N.
#Вычислить выражение вида: x ^ n / n!.
