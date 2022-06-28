import sys
input = sys.stdin.readline
print = sys.stdout.write

num = int(input())
list = [list(input().split()) for _ in range(num)]



list.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in list:
    print(str(i[0]) + '\n')