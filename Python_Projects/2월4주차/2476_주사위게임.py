enter = int(input())

total = 0 
total1 = 0
for i in range(enter):
    a, b, c = map(int, input().split())
    if a==b and b==c:
        total=max(total, 10000+a*1000)
    elif a!=b and b!=c and c!=a:
        total = max(max(a,b,c) * 100, total)
    elif a==b or b==c:
        total = max(1000 + b * 100, total)
    else:
        total = max(1000 + c * 100, total)
    
print(total)
        