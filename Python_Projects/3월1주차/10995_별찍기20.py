num = int(input())
for i in range(1, num + 1):
    if i % 2 == 0:
        temp = ' ' + '* ' * num
    else:
        temp = '* ' * num
    print(temp)