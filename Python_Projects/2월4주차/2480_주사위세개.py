temp = list(map(int, input().split()))

if temp[0]==temp[1] and temp[1]==temp[2]:
    print(10000+temp[0]*1000)
elif temp[0]==temp[1] and temp[1]!=temp[2]:
    print(1000+temp[0]*100)
elif temp[0]!=temp[1] and temp[1]==temp[2]:
    print(1000+temp[1]*100)
elif temp[0]==temp[2] and temp[1]!=temp[2]:
    print(1000+temp[2]*100)
elif temp[0]!=temp[1] and temp[1]!=temp[2] and temp[2]!=temp[0]:
    temp.sort()
    print(temp[2]*100)