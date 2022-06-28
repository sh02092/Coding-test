num = int(input())
for i in range(1, num + 1):
    temp = ' '*(num-i)+'*'*i
    print(temp)
for i in reversed(range(1, num)):
    temp = ' '*(num-i)+'*'*i
    print(temp)