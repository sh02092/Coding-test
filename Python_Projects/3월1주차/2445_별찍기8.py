num = int(input())

for i in range(1, num + 1):
    temp = '*' * i + ' ' * (2 * (num - i)) + '*' * i
    print(temp)

for i in reversed(range(1, num)):
    temp = '*' * i + ' ' * (2 * (num - i)) + '*' * i
    print(temp)
