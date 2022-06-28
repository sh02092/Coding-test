num = int(input())

a0 = 0
a1 = 1
arr = []
arr.append(0)
arr.append(1)
for i in range(1, num):
    arr.append(arr[i-1] + arr[i])

print(arr[-1])