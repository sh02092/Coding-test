import sys
input = sys.stdin.readline

import copy
from collections import Counter
from itertools import combinations_with_replacement
li = [1,1,1,2,2,2,2,2,1,3,3,3,3,4,4,1,1,1,2,2,5,5,8]
li1 = [3,2,1]
print(Counter(li)[7])
print(list(combinations_with_replacement(li1, 2)))

li.sort(key=lambda x:x)
print(li)

li1 = [3,2,1]
li4 = li1
li3 = li1.copy()
li2 = copy.deepcopy(li1)
li1[1] = 5

print(li1)
print(li2)
print(li3)
print(li4)

setLi = set(li)
print(setLi)
setLi = list(setLi)
del setLi[1]
print(setLi)