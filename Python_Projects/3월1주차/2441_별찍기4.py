num = int(input())
for i in reversed(range(1, num + 1)):
    temp = '*' * i
    print(temp.rjust(num))