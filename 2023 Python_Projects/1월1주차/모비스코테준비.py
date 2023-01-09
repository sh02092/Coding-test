

str = 'hello world'
print(str.find('a'))
print(str.replace('hello', 'Hello'))
print(str.upper())
print(str.lower())
print(' '.join(str))
print(str.capitalize())
print(str.count('h'))
print(str)

a = list(bin(10))
print(a.count('1'))

list_1 = [[0,"A"],[4,"B"],[2,"C"]] 
list_1.sort(key = lambda x:x[0])
list_1.sort(key = lambda x:x[1], reverse=True)
list_2 = list_1.copy()
list_3 = list_2.sorted(list_1, key=lambda x:x[0])
print(list_1)

class Node:
    def __init__(self):
        self.prev = -1
        self.next = -1
        self.is_delete = False

nodeList = [Node() for _ in range(5)]
for i in range(5):
    nodeList[i].next = i+1
    nodeList[i+1].prev = i