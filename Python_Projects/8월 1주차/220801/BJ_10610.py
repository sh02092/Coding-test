n = list(input())
n.sort(reverse=True)
sum=0
for i in n:
    sum += int(i)
if sum % 3 != 0 or n[-1] != '0':
    print(-1)
else:
    print(''.join(n))