a = int(input())
s = list(map(int,input().split()))
c = 0

for run in range(a-1):
    for i in range(a-1):
        if s[i] > s[i+1]:
            c+=1
            s[i], s[i+1] = s[i+1], s[i]
for i in s:
     print(i, end=' ')
print()
print(c)


           #d.append(s[i+1])
            #s.pop(1)
           # print(s[i+1],s[i])
       
            #print(s[i],s[i+1])
            #d.append(s[i])
            #s.pop(0)
            
        #print(d)
    #
        
    #d == s[:]
        #if i > i+1:
            #n.append(s[i+1])
        #n.append(s[i])
            
           # s = s[1:]
        #s[i] == s[i+1]
        #s[i+1] == s[i]
        #print(s[1])
            #print(s)
            #print(n)

        
