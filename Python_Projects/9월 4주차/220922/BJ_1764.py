# https://www.acmicpc.net/problem/1764
# 듣보잡- BJ_1764

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_name = [[] for _ in range(n)]
answer = []

for i in range(n):
    n_name[i] = input()
for i in range(m):
    m_name = input()
    for j in range(len(n_name)):
        if m_name==n_name[j]:
            answer.append(m_name)
            n_name.pop(j)
            break

print(len(answer))
answer.sort()
print(''.join(answer))