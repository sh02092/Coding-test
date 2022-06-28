num = int(input())
# arr = [1 for i in range(num)]
count = 0 
for i in range(1, num + 1):
    if i < 100:
        count += 1
    else:
        arr = []
        while i >= 10:
            arr.append(i % 10)
            i //= 10
        arr.append(i % 10)
        for j in range(1, len(arr)):
            temp = arr[1] - arr[0]
            if arr[j] - arr[j - 1] == temp:
                if j == len(arr) - 1:
                    count += 1
print(count)