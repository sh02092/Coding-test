# https://www.acmicpc.net/problem/14681
# 사분면 고르기- BJ_14681

import sys
input = sys.stdin.readline

x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)