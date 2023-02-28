# https://www.acmicpc.net/problem/1110
# 더하기 사이클- BJ_1110

import sys
input = sys.stdin.readline

n = int(input())
nn = n
ans = 0

while 1:
    ans += 1
    newN = (nn%10) * 10 + (nn//10 + nn%10) % 10
    if newN == n:
        break
    nn = newN

print(ans)