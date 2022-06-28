h, w = map(int, input().split())
graph=[]
for i in range(h):
    graph.append(input())

temp=[[-1]*w for _ in range(h)]

for i in range(h):
    count = 0
    babo = False
    for j in range(w):
        if graph[i][j]=='c':
            count = 0
            babo = True
            temp[i][j] = count
        elif graph[i][j]=='.' and babo==True:
            count+=1
            temp[i][j] = count
for i in range(h):
    print(*temp[i])
        