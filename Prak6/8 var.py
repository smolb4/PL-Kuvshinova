print ('Вариант 8')
print ('Задание 1')

mas=[1, 2, 3, 4, 5]
print('Элементы массива: ', mas)

summ = sum(mas)
print('Сумма элементов массива: ', summ)

o=1
for i in range(len(mas)):
    o *= (mas[i])
print('Произведение элементов массива: ', o)

print ('Задание 2')

mass=[1, 0, 2, 3, 4, 5]
sr = sum(mass)/ len(mass)
print('Среднее арифметическое списка:', sr)
for k, x in enumerate(mass):
    if x==0:
        mass[k]=sr
print(mass)
