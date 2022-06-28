num = []
for _ in range(int(input())):
    name, day, month, year = input().split()
    num.append([name, int(day), int(month), int(year)])

num.sort(key = lambda x:(x[3], x[2], x[1]))
print(num[-1][0])
print(num[0][0])