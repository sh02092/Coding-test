time=int(input())

if time%10!=0:
    print(-1)
else:
    a = time // 300
    time%=300
    b = time // 60
    time %=60
    c = time //10

    print(a,b,c)