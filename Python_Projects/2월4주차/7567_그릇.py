num = list(input())

total = 10
for i in range(len(num)-1):
    if num[i]==num[i+1]:
        total+=5
    else:
        total+=10

print(total)