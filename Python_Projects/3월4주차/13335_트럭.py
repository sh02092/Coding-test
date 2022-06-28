from collections import deque
import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())
temp = list(map(int, input().split()))

q = deque()
for i in range(n):
    q.append(temp[i])
    if sum(q) > l or len(q) > w:
        q.pop()
    
