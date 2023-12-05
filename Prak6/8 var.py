print ('Вариант 8')
print ('Задание 1')
n = int(input('Кол-во чисел в массиве: '))
mas = [] #создаем пустой массив
for i in range(n):
    mas.append(int(input('Числа в массиве: '))) #заполняем массив
pr=1
s = sum(mas)
for j in mas:
    pr*=j
print(s, pr)
#1. Найдите сумму и произведение элементов списка. Результаты вывести на
#экран.

print ('Задание 2')
n = int(input('Кол-во чисел в массиве: '))
mas = [] #создаем пустой массив
for i in range(n):
    mas.append(int(input('Числа в массиве: '))) #заполняем массив

a = float(sum(mas)/len(mas))
print(a)
for j in range(len(mas)):
    if mas[j]==0:
        mas[j]=a
print(mas)
#2. В массиве действительных чисел все нулевые элементы заменить на среднее
#арифметическое всех элементов массива.
