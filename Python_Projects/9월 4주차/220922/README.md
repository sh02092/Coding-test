# Solving

## 숫자의 표현
https://school.programmers.co.kr/learn/courses/30/lessons/12924
### 문제풀이
```python
def solution(n):
    count = 1
    x = 2   # 2부터
    if n > 3:
        while x < n//2:
            if x % 2 == 1:              # 홀수로 나눌 때
                if n == n//x * x:       # 나눠지면
                    if n//x - x//2 > 0:
                        count += 1
            else:                       # 짝수로 나눌 때
                if n/x - 0.5 == n//x: # 조건 만족하면
                    if x//2 < n/2 and n/x - x/2 > 0:
                        count += 1
            x += 1    
    elif n==3:
        count = 2
    return count
```
조건에 맞게 구현한다.
### 의견
문제 조건에 맞게끔 조건을 구현했다. 야매로 푼 문제, 깔끔하진 않다.