temp = []
for i in range(9):
    a = int(input())
    temp.append(a)

print(max(temp))
print(temp.index(max(temp)) + 1)