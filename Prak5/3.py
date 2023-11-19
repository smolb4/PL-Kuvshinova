s = input()
c = m = 0

for i in range(len(s)):
    if s[i] == 'н':
        c+=1
        m=max(m,c)
    else:
        c=0
print(m)  #самая длинная последовательность

s = s.replace('!','.')
print(s)  #полученная строка
