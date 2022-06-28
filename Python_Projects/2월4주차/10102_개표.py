num = int(input())

count_A=0
count_B=0

word = input()

count_A += word.count('A')
count_B += word.count('B')

if count_A > count_B:
    print("A")
elif count_A == count_B:
    print("Tie")
else:
    print("B")