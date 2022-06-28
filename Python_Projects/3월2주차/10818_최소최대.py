num = int(input())
list = list(map(int, input().split()))
list.sort()
print('%d %d' % (list[0], list[-1]))