num = int(input())
for i in range(num):
    temp = '*' * (i + 1)
    print(temp.rjust(num))