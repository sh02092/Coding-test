import sys
total = 0
for _ in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    total += (a - 1)
print(total + 1)