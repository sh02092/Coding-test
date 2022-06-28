a, b = map(int, input().split())
arr = []
for i in range(1, a + 1):
    if a % i == 0:
        arr.append(i)
if b > len(arr):
    print(0)
else:
    print(arr[b-1])