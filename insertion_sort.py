a = int(input())
s = list(map(int,input().split()))
for j in range(1, a):
    key = s[j] #текущий элемент списка
    i = j-1 #индекс предшеств.элемента
    while i >= 0 and s[i] > key: #пока эл-т меньше предшеств эл-та списка
        s[i+1] = s[i] #эл-т двигается влево
        i = i-1 
        s[i+1] = key #переходим к след элементу списка внутри цикла
    #print()
   #print(i, s[i], key, s[i+1])
print(*s)
            
      
