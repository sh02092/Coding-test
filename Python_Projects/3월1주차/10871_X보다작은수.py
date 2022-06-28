from posixpath import split


a, b = map(int, input().split())
arr = []
temp = list(map(int, input().split()))
for i in range(a):
    if temp[i] < b:
        arr.append(temp[i])

for i in range(len(arr)):
    print(arr[i], end = ' ')