word=input()
for i in range(0, len(word), 10):
    temp = i + 10
    print(word[i : temp])
