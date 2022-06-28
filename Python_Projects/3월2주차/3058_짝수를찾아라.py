for _ in range(int(input())):
    li = list(map(int, input().split()))
    total = 0
    temp = []
    for i in range(len(li)):
        if li[i] % 2 == 0:
            temp.append(li[i])
    temp = sorted(temp)
    print(sum(temp), end = ' ')
    print(temp[0])