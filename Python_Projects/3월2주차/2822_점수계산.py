li = [int(input()) for _ in range(8)]
sorted_li = sorted(li, reverse=True)
t = sum(sorted_li[:5])
idx_li = sorted([li.index(sorted_li[i])+1 for i in range(5)])
print(t)
print(*idx_li)