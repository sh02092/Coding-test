while(1):
    num = int(input())
    if num==-1:
        break
    else:
        temp=[]
        for i in range(1, num):
            if num%i==0:
                temp.append(i)
    if sum(temp)==num:
        print(num, " = ", " + ".join(str(i) for i in temp), sep="")
    else:
        print("%s is NOT perfect."%num)