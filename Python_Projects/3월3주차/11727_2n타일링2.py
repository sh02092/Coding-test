import sys
input=sys.stdin.readline

temp = [0, 1, 3]
n = int(input())
if n > 2:
    for i in range(3, n + 1):
        temp.append(temp[i - 2] * 2 + temp[i - 1])
print(temp[n]%10007)

# 1. 2x(N-1)만큼 타일링하고 2x1 타일을 붙인다.

# 2-1. 2x(N-2)만큼 타일링하고 1x2 타일을 두 개 붙인다.

# 2-2. 2x(N-2)만큼 타일링하고 2x2 타일을 한 개 붙인다.