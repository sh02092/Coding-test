for _ in range(int(input())):
    total = 0
    car = int(input())
    for _ in range(int(input())):
        a, b = map(int, input().split())
        total += a*b
    total += car
    print(total)