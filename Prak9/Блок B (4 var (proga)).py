print ('Задание 4')

print ('Блок B')

def pomogite(x, d=0):
    if d==0:
        d= x - 1
    while d >= 2:
        if x%d==0:
            return print('NO')
        else:
            pomogite(x, d-1)
    else:
        return print('YES')
    pass
n = int(input('Введите число (>1): '))
pomogite(n)

#4. Дано натуральное число n>1. Проверьте, является ли оно простым.
#Программа должна вывести слово YES, если число простое и NO, если
#число составное.
