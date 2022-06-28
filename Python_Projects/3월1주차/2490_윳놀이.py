for _ in range(3):
    temp = list(map(int, input().split()))
    if temp.count(1) == 0:
        print('D')
    elif temp.count(1) == 1:
        print('C')
    elif temp.count(1) == 2:
        print('B')
    elif temp.count(1) == 3:
        print('A')
    elif temp.count(1) == 4:
        print('E')