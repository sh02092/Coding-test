for _ in range(int(input())):
    num, sit = map(int, input().split())
    temp = [False] * (sit + 1)
    count = 0
    for _ in range(num):
        a = int(input())
        if temp[a] == False:
            temp[a] = True
        else:
            count += 1
    print(count)