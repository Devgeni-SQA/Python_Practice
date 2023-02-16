l=[]
for i in range(int(input())):
    s = input()
    if not 'соль' in s.split():
        l.append(s)
print(*l,sep=', ')
        
