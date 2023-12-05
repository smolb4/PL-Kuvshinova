from random import randint
a=[]
n=int(input('Строчки: ')) #строчки
m=int(input('Столбцы: ')) #столбцы
for i in range(n):
    b=[]
    for j in range(m):
        b.append(randint(1,100))
    a.append(b)

f=open('Kuvshinova_Anastasia_Alekseevna_UB-31_vvod.txt','w+')
for i in a:
    f.write(str(i), )
    f.write('\n')

f.close()

max1=0
min1=1
for i in a:
    min1=i.index(min(i))
    max1=i.index(max(i))
    i[max1],i[0]=i[0],i[max1]
    i[min1],i[-1]=i[-1],i[min1] # обмен 2-ух переменных через временный кортеж

f=open('Kuvshinova_Anastasia_Alekseevna_UB-31_vivod.txt','w+')
for i in a:
    f.write(str(i), )
    f.write('\n')

f.close()
