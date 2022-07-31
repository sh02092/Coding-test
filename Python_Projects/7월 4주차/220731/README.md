# Solving

## 거스름돈- BJ_5585
https://www.acmicpc.net/problem/5585
### 문제풀이
```python
n = int(input())
n = 1000 - n
count = 0
if n >= 500:
    count += n // 500
    n -= 500 * (n // 500)
if n >= 100:
    count += n // 100
    n -= 100 * (n // 100)
if n >= 50:
    count += n // 50
    n -= 50 * (n // 50)
if n >= 10:
    count += n // 10
    n -= 10 * (n // 10)
if n >= 5:
    count += n // 5
    n -= 5 * (n // 5)
count += n
print(count)
```
입력한 수를 1000에서 뺀 후 500엔부터 1엔까지 차례로 비교하며 받을 잔돈 개수를 count한다.
### 의견
쉬운 그리디 알고리즘 문제