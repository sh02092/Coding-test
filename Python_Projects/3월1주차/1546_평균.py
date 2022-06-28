num = int(input())
grade = list(map(int, input().split()))
max_grade = max(grade)
total = 0
for i in range(len(grade)):
    total += grade[i] / max_grade * 100
print(total/len(grade))