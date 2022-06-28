score = []
compare = []
for i in range(5):
    total = 0
    score = list(map(int, input().split()))
    for i in range(len(score)):
        total += score[i]
    compare.append(total)
print(compare.index(max(compare)) + 1, max(compare))