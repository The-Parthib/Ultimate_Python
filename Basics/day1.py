# print("hello world")
# print("Namaste Duniya")
# print("Hello Howrah Bashi")

# for i in range(5):
#     print("Love with Heart")

# a = [1,2,3,4,5]
# print(type (a))

# a.append(76)
# a.append(77)
# a.append(78)
# print(a)

# ++++++++++++++

# x=2
# y=4.6

# res = x+y;
# print(type(res))

# ++++++++++++++

# hello = "rupsaa".upper()
# hello = "RUPSA".lower()
# hello = "parthib panja"
# print(hello.lower())
# print(hello.capitalize())

# str = "lollipop"
# print(str.count('l'))
# print(str.find('i')) #return index

# +++++++++++++
'''
a  = "hello "
b=3
c="world"
print(a*b)
print(a+c)
print('ad'>'ab')
print(ord("a")> ord("Z"))
'''

'''
a=["hello", 12, True]
# a.pop(2)
# print(a[0])
# # a.append("good night")
# a.extend([4,5,7,8,"love","study"])
# print(len(a))
# print(a)
# b="hello"
# print(len(b))
b=a[:] # a list is copied to the list b
a[0] = "bolo"
print(a,b)
print(type(a))

z=(1,2,3,4,True,"Goal")
print(type(z))
z.append("a")
print(z)
'''

'''
x=[1,2,3,4,5,6,7,"hello"]
for i in range(len(x)):
    print(x[i])

x=[1,2,3,4,5,6,7,"hello"]
for i in x:
    print(i)

'''

'''
x=['hel', "rup", 1,2,3]

for i, element in enumerate(x):
    print(i, element)

'''

'''
i=0

while True:
    print("run", i)
    i+=1
    if i==10:
        break

'''

# +++++++++ slice +++++++++
'''
x = [0,1,2,3,4,5,6,7,8]
y = ['hi','hello','goodbye','cya','sure']
z=(5,6,7,8,9)
s = "hello"

# sliced = x[0:4:2]
sliced = z[1::-1]
print(sliced)
'''

# +++++++ set +++++++
'''
s = set()
x = {32,4,3,4,2,2,2,3}
y={33,1,2,32,4,6,5}
print(type(x))
print(y.difference(x))
print(2 in x)
'''

# +++++++ Dictionaries ++++++++
'''
x = {"key":4,"key2":5}
print("key" in x)
print(list(x.keys()))

for key,value in x.items():
    print(key, value)

print()
for key in x:
    print(key, x[key])
'''

# +++++++++ comprehensions ++++++++

arr = [i for i in range(10)]
print(arr)

arr2 = [[j for _ in range(5)] for j in range (3)]
print(arr2)