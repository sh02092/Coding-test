import sys
input = sys.stdin.readline
n = int(input())
n_ = [int(input()) for _ in range(n)]
n_ = sorted(n_)
for i in n_:
    print(i)