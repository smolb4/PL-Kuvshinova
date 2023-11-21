print ('Задание 3')

print ('Блок А')

def obratka (x):
    if x:
        return obratka(x[1:])+[x[0]]
    else:
        return []
o = obratka(list(input('Введите цифру: ')))
print(''.join(o))

#3. Вывести число в обратном порядке
