k=0
s = input()
while ('.' in s):
    s=s.replace ('.','',1)
    k+=1
print(k)
