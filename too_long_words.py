for i in range(int(input())):
    s = input()
    if len(s)<11:
        print(s)
    else:
        print(s[0],len(s)-2,s[-1], sep='')
    
