li = []
for _ in range(int(input())):
    a = int(input())
    if a == 0:
        li.pop()
    else:
        li.append(a)
print(sum(li))
    