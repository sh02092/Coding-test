num = int(input())
temp = list(map(int, input().split()))

temp = sorted(temp)
print(temp[0] * temp[-1])