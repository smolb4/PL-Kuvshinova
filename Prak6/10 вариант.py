from random import randint

print('Вариант 10')
print('Задание 1')
n = randint(4, 10)
d = []
for i in range(n):
    d.append(randint(1, 10))
print(d)
povtor = []
for i in d:
    if d.count(i)>1 and i not in povtor:
        povtor.append(i)
    else:
        pass
if len(povtor)==0:
    print('Повторяющиеся элементы в списке отсутствуют')
else:
    print(povtor)
#1. Определите, есть ли в списке повторяющиеся элементы, если да, то вывести
#на экран это значение, иначе сообщение об их отсутствии

print('Задание 2')
m1 = 15
a = []
for i in range(m1):
    a.append(randint(1, 30))
print('Первоначальный массив: ', a)
for i in range(len(a)):
    if a[i]<10:
        a[i]=0
    elif a[i]>20:
        a[i]=1
    else:
        pass
print('Преобразованный массив: ', a)


#2. Дан одномерный массив из 15 элементов. Элементам массива меньше 10
#присвоить нулевые значения, а элементам больше 20 присвоить 1. Вывести на
#экран монитора первоначальный и преобразованный массивы в строчку