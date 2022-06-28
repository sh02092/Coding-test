from collections import deque
import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())
temp = deque(map(int, input().split()))
q = deque([0 for _ in range(w)])
count = 0

while q:
    if temp:
        q.popleft()
        if sum(q) + temp[0] <= L:
            q.append(temp.popleft())
            count += 1
        else:
            q.append(0)
            count += 1
    else:
        q.popleft()
        count += 1
print(count)