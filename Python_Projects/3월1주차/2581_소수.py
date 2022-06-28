a = int(input())
b = int(input())
total = 0
arr = []
for i in range(a, b + 1):
    for j in range(2, i + 1):
        if i % j == 0:
            if i == j:
                arr.append(i)
                total += i
            else:
                break
    
if len(arr) == 0:
    print(-1)
else:
    print(total)
    print(arr[0])