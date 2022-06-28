li = [int(input())for _ in range(9)]

total = sum(li)
for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if (total - (li[i] + li[j])) == 100:
            a = li[i]
            b = li[j]
            li.remove(a)
            li.remove(b)
            break
    if len(li)< 9:
        break
li = sorted(li)
for i in range(len(li)):
    print(li[i])