for _ in range(int(input())):
    li = list(map(int, input().split()))
    li = sorted(li, reverse=True)
    print(li[2])
