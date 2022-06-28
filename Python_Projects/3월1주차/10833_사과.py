total = 0 
for _ in range(int(input())):
    a, b = map(int, input().split())
    total += b % a

print(total)