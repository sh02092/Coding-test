num = list(map(int, input().split()))

while num != [1, 2, 3, 4, 5]:
    for i in range(5 - 1):
        if num[i]>num[i + 1]:
            num[i], num[i + 1] = num[i + 1], num[i]
            print(*num)
    
    # if num[0] > num[1]:
    #     num[0], num[1] = num[1], num[0]
    #     print(*num)
    # if num[1] > num[2]:
    #     num[1], num[2] = num[2], num[1]
    #     print(*num)
    # if num[2] > num[3]:
    #     num[2], num[3] = num[3], num[2]
    #     print(*num)
    # if num[3] > num[4]:
    #     num[3], num[4] = num[4], num[3]
    #     print(*num)
    