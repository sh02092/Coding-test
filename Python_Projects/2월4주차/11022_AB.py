T=int(input())

for i in range(T):
    a,b=input().split()
    a=int(a)
    b=int(b)
    print("Case #%s: %s + %s = %s"%(i+1, a, b, a+b))