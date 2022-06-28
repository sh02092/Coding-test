test = int(input())

for i in range(test):
    quiz = list(input())
    total=0
    reward=0
    for i in range(len(quiz)):
        if quiz[i]=='X':
            reward=0
        elif quiz[i]=='O':
            reward+=1
        total+=reward
    print(total)