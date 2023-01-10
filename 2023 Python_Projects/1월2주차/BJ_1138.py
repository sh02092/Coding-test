# https://www.acmicpc.net/problem/1138
# 한 줄로 서기- BJ_1138

import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
graph = list(False for _ in range(n))
ansLi = list(0 for _ in range(n))
cnt = 0

for j in range(len(li)):
    for i in range(len(li)):
        if graph[i] == True:    # 이미 존재하는 경우 넘기기
            continue
        else:   # 존재하지 않는 경우
            if cnt == li[j]:    # 왼쪽에 존재하는 사람 수를 세었을 때 입력한 값과 같은 경우
                graph[i] = True
                ansLi[i] = j + 1
                cnt = 0
                break
            else:       # 왼쪽에 존재하는 사람 수를 세었을 때 입력한 값과 다를 경우
                cnt += 1
print(*ansLi)