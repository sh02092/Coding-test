n = int(input())
m = int(input())
temp=[]

while m >= 10:
    temp.append(m%10)
    m //= 10
temp.append(m)
print(sum(temp))