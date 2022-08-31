# Solving

## 이진 변환 반복하기
https://school.programmers.co.kr/learn/courses/30/lessons/70129
### 문제풀이
```python
def solution(s):
    answer = []
    count_0 = 0
    count = 0
    while s!='1':
        count_1 = 0 
        for i in s:
            if i == '1':
                count_1 += 1
            else:
                count_0 += 1
        s = ''
        while 1:
            if count_1 <= 1:
                break

            if count_1 % 2 == 0:
                s += '0'
            else:
                s += '1'
            count_1 //= 2
        s += str(count_1)
        count += 1
    
    answer.append(count)
    answer.append(count_0)

    return answer

s = "110010101001"
print(solution(s))
```
s가 1이 될 때까지 0을 지우고, 1의 개수를 새며 이진수를 만들기를 반복한다. 이 때, 이진수를 만드는 과정에서 순서를 거꾸로 입력한다. 예를들어 6을 이진수로 바꿀 때 '110'이 아닌'011'로 넣는다.
### 의견
어렵지 않은 문제였다.


## 소수&팰린드롬
https://www.acmicpc.net/problem/1747
### 문제풀이
```python
import math

n = int(input())
max_pal = 0

if n > 1:
    for i in range(n, 1000000000001):
        br = False

        # 소수 판별
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                br = True
                break
        if br:
            continue
        
        # 팰린드롬인 수 판별
        temp = str(i)
        if len(temp) > 1:
            for j in range(len(temp)//2 + 1):
                if temp[j] != temp[-(j + 1)]:
                    br = True
                    break
        if br:
            continue
        max_pal = i
        break
else:
    max_pal = 2

print(max_pal)
```
가능한 큰 수까지 소수 판별을 하며 소수라면 팰린드롬인 수를 판별한다. 발견한 팰린드롬인 수 중 가장 처음 발견한 수를 출력한다.
### 의견
문제 이해를 잘못했다. 조건을 만족하는 수의 범위가 1,000,000 까지인 줄 알았지만 엄청 큰 수를 입력하여 해결했다.