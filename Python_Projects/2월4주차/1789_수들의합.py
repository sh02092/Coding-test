n = int(input())

temp = 0
total = 0
if n == 1:
    print(1)
else :
    while total <= n:
        temp = temp + 1
        total = total + temp

    print(temp-1)