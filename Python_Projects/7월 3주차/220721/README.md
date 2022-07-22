# Solving

## 다리놓기- BJ_1010
https://www.acmicpc.net/problem/1010
### 문제풀이
```python
def factorial(num):
    total = 1
    for i in range(1, num + 1):
        total *= i
    return total

for _ in range(int(input())):
    n, m = map(int, input().split())
    if m - n == 0:
        print(1)
    else:
        print(factorial(m) // (factorial(m - n) * factorial(n)))    
```
m 콤비네이션 n
### 의견
다리가 겹치면 안된다 하여 다리 위에 다리가 놓이면 안되는 문제인줄 알았다. 하지만 예제 출력을 보니 너무 터무니 없는 숫자를 봤고, 조금 다시 생각해보니 단순히 다리 자체가 겹치지만 않으면 된다. 다리가 겹쳐도 되는 경우는 퍼뮤테이션을 사용하면 되고, 겹치면 안되므로 콤비네이션만 사용하면 간단하게 풀리는 문제였다.