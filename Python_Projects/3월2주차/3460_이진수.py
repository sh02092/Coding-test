for _ in range(int(input())):
    num = int(input())
    list = []
    while num > 0:
        list.append(num % 2)
        num //= 2
    n = -1
    while 1:
        if list[n+1:].count(1)==0:
            break
        n += list[n+1:].index(1) + 1
        print(n, end=' ')