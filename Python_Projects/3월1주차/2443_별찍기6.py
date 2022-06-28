num = int(input())
for i in reversed(range(1, num + 1)):
    temp = ' ' * (num - i) + '*' * ((i * 2) - 1)
    print(temp)