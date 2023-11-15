print ('Вариант 4')
print ('Задание 1')

mas=[1, 2, 8, 3, 4, 5]
print('Элементы массива: ', mas)

k=0
max_el = max(mas)
print('Максимальный элемент массива: ', max_el)
for max_el in mas:
 k=k+1
 if max_el==max(mas):
    print('Порядковый номер максимального элемента массива: ', k)

print ('Задание 2')
mass=[]
for h in mas:
 if h%2!=0:
    mass.append(h)
 elif mass==[]:
    print('Нет нечетных')
print(mass)