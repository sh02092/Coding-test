# Solving

## 로프- BJ_2217
https://www.acmicpc.net/problem/2217
### 문제풀이
```python
n = int(input())
rope = []
max_ = []
for _ in range(n):
    rope.append(int(input()))
rope = sorted(rope)

for i in range(n):
    max_.append(rope[i] * (n - i))
print(max(max_))
```
들수 있는 중량이 가장 낮은 로프를 n개 사용할 때부터 중량이 가장 높은 로프 1개 사용할 때까지 모든 경우의 수를 비교하여 가장 최대의 중량을 들 수 있는 경우를 출력한다.
### 의견
쉬운 그리디 알고리즘 문제


## 30- BJ_10610
https://www.acmicpc.net/problem/10610
### 문제풀이
```python
n = list(input())
n.sort(reverse=True)
sum=0
for i in n:
    sum += int(i)
if sum % 3 != 0 or n[-1] != '0':
    print(-1)
else:
    print(''.join(n))
```
내림차순 정렬하여 3의 배수인지, 0을 갖고 있는지 판단한다.
### 의견
문자열에서 숫자로 한번에 만드는 join() 함수를 알게 되었다.