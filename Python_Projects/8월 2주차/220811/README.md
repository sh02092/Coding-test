# Solving

## 기지국 설치
https://school.programmers.co.kr/learn/courses/30/lessons/12979
### 문제풀이
```python
from math import ceil

def solution(n, stations, w):
    answer = 0
    # 기지국이 전파 전달 가능한 범위
    w_range = 2 * w + 1
    start = 1

    # 기지국 전파 전달이 안되는 범위에 대해
    # 전달 가능한 범위로 나눈 값을 올림해 answer에 더하고, 
    # 시작 지점을 전파 전달 가능한 범위의 끝으로 옮긴다.
    for s in stations:
        answer += max(ceil((s - w - start)/w_range), 0)
        start = s + w + 1
    
    # 기존에 있던 모든 기지국에 대해
    # 기지국들 앞의 전파 전달을 마친 이후
    # 뒤의 남아있는 아파트들에 대해 전파 전달이 안되는 경우
    # 전달 가능한 범위로 나눈 값을 올림해 answer에 더한다.
    if n >= start:
        answer += ceil((n - start + 1)/w_range)

    return answer

n, w = map(int, input().split())
stations =[4, 11]
print(solution(n, stations, w))
```
기지국이 전파 전달 가능한 범위를 구해 기존에 설치되어 있는 기지국들 사이의 아파트들에 대해 전파 전달 가능한 범위로 나눈 값을 올림 하여 더한다. 기존해 설치되었던 기지국 중 마지막 기지국에 대해서는 전체 아파트 수보다 작을 경우 끝에 남은 아파트들에 대해 전파 전달 가능한 범위로 나눈 값을 올림해 한번 더 더한다.
### 의견
시간복잡도를 해결하는 문제였다. 접근 방식이 틀렸던 것은 아니었지만 프로그래머스 Level 3 인만큼 어려운 문제일 것이다라는 생각에 지배되어 돌아돌아 생각하게 된 문제였다. 알고보니 전파 전달이 안되는 아파트들에 대해 전파 전달 가능한 범위로 나눠 올림한 값들을 더하면 해결되는 어렵지 않은 문제였다.