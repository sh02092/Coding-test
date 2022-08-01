n = int(input())
rope = []
max_ = []
for _ in range(n):
    rope.append(int(input()))
rope = sorted(rope)

for i in range(n):
    max_.append(rope[i] * (n - i))
print(max(max_))