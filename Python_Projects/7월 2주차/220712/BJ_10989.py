import sys
input = sys.stdin.readline

n = int(input())

# 미리 list를 만들어놓는다.
# append를 사용할 경우 메모리 재할당이 이루어져 
# 속도 저하가 일어나고, 효율적이지 못하다.
n_ = [0 for _ in range(10001)]
for _ in range(n):
    n_[int(input())] += 1

for i in range(len(n_)):
    if n_[i] != 0:
        for _ in range(n_[i]):
            print(i)