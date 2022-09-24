# https://www.acmicpc.net/problem/8979
# 올림픽- BJ_8979

n, k = map(int, input().split())
country = [[] for _ in range(k + 1)]

for i in range(n):
    c, gold, silver, bronze = map(int, input().split())
    country[c] = [gold, silver, bronze, c]
country.sort(key=lambda x:x[0])
country.sort(key=lambda x:x[1])
country.sort(key=lambda x:x[2])

print(country.index())