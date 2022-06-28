num = int(input())

for i in range(num):
    li = list(map(int, input().split()))
    li.remove(min(li))
    li.remove(max(li))
    li = sorted(li)
    if li[-1] - li[0] >= 4:
        print('KIN')
    else:
        print(sum(li))