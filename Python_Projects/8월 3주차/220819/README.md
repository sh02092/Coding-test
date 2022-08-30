# Solving

## 줄어들지 않아
https://www.acmicpc.net/problem/2688
### 문제풀이
```python
n = [[1,1,1,1,1,1,1,1,1,1]]
n_sum = [10]

for i in range(64):
    n_sub = []
    for j in range(10):
        sub_total = 0
        for k in range(j, 10):
            sub_total += n[i][k]
        n_sub.append(sub_total)
    n.append(n_sub)
    n_sum.append(sum(n_sub))

t = int(input())
for _ in range(t):
    print(n_sum[int(input()) - 1])
```
n list에 10개로 이루어진 list를 모두 더하면 n list의 index + 1에 해당하는 줄어들지 않는 자리 수의 개수이다. 10개로 이루어진 list는 이전 10개짜리 list에서 10개 모두 더한 값부터 맨 앞 index의 값부터 하나씩 빼가며 마지막에는 마지막 index의 값 만을 list에 넣어 총 10개짜리의 list를 만들어 n list에 넣는다. n의 범위가 64까지이므로 문제 입력 전에 미리 만들어 놓고 테스트 케이스를 진행한다. 
### 의견
규칙을 찾기가 좀 까다로웠다. 헷갈렸다.. 시간 복잡도는 이전에 비슷한 문제를 풀어봤기에 64까지의 모든 경우를 먼저 만들어 놓고 테스크 케이스를 진행하여 해결했다.


