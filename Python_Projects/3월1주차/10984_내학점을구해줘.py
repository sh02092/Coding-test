for _ in range(int(input())):
    total = 0
    stu = 0.0
    for _ in range(int(input())):
        a, b = map(float, input().split())
        stu += a
        total += a * b
    total /= stu
    print('%d %s'%(stu, round(total,1)))