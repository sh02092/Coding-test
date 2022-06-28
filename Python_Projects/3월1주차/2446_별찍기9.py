num = int(input())

for i in range(1, num + 1):
    temp = ' ' * (i - 1) + '*' * ((2 * (num - (i - 1))) - 1)
    print(temp)
for i in reversed(range(1, num)):
    temp = ' ' * (i - 1) + '*' * ((2 * (num - (i - 1))) - 1)
    print(temp)