num = int(input())
for i in range(1, num + 1):
    # center = num * 2 - 1
    temp = i * 2 - 1
    total = ' ' * (num - i) + '*' * temp
    print(total)