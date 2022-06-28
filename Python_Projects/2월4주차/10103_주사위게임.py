num = int(input())

total_a=100
total_b=100
for i in range(num):
    a, b = map(int, input().split())
    if a==b:
        continue
    elif a>b:
        total_b-=a
    elif a<b:
        total_a-=b
    
print("%s\n%s"%(total_a, total_b))
