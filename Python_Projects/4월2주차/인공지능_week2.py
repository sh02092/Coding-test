x = 3
print(x,type(x))

print(x+1)
print(x-1)
print(x*2)
print(x**2)

x+=1
print(x)
x*=2
print(x)

y=2.5
print(type(y))
print(y,y+1,y*2,y**2)

t, f = True, False
print(type(t))

print(t and f)
print(t or f)
print(not t)
print(t != f)

hello='hello'
world='world'
print(hello, len(hello))

s="hello"
print(s.capitalize())
print(s.upper())
print(s.replace('l', '(ell)'))
print('   world'.strip())

xs = [3,1,2]
print(xs,xs[2])
print(xs[-1])

xs[2]='foo'
print(xs)

xs.append('abc')
print(xs)

x=xs.pop()
print(x,xs)

nums = list(range(5))
print(nums)
print(nums[2:4])

animals = ['cat', 'dog', 'monkey']
for i in animals:
    print(i)

for idx, animal in enumerate(animals):
    print('#{}: {}'.format(idx+1, animal))

d = {'cat': 'cute', 'dog': 'furry'}
print(d)
print(d['cat'])

d['fish'] = 'wet'
print(d)

print(d.get('monkey', 'N/A'))
print(d)
del d['fish']
print(d.get('fish', 3))

d = {'person': 2, 'cat': 4, 'spider': 8}
print(d)
for animal, legs in d.items():
    print('A {} has {} legs'.format(animal, legs))