print ('Задание 4')

print ('Блок B')

def pomogite(n, div=None):
    if div is None:
        div= n - 1
    while div >= 2:
        if n%div==0:
            print('NO')
            return n
        else:
            return pomogite(n, div-1)
    else:
        print('YES')
        return True
n = int(input('Введите число (>1): '))

#4. Дано натуральное число n>1. Проверьте, является ли оно простым.
#Программа должна вывести слово YES, если число простое и NO, если
#число составное. 
