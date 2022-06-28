from collections import deque
import sys
input=sys.stdin.readline

def left(num, dir):
    if num<0 or temp[num][2]==temp[num+1][6]:
        return
    
    if temp[num][2]!=temp[num+1][6]:
        left(num-1,-dir)
        temp[num].rotate(dir)

def right(num, dir):
    if num>3 or temp[num][6]==temp[num-1][2]:
        return

    if temp[num][6]!=temp[num-1][2]:
        right(num+1,-dir)
        temp[num].rotate(dir)

input_list = [list(map(str, input())) for _ in range(4)]
temp=deque(deque() for _ in range(4))
for i in range(4):
    for j in range(8):
        temp[i].append(int(input_list[i][j]))

for _ in range(int(input())):
    num, dir = map(int, input().split())
    num -= 1
    right(num + 1, -dir)
    left(num - 1, -dir)
    temp[num].rotate(dir)

total = 0
for i in range(4):
    if temp[i][0] == 1:
        total += 2 ** i
print(total)