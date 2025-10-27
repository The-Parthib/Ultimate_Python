'''
# list = [i for i in range(10)]
# print(list)

# list = [6]*6
# print(list)

list = [2,4,9,1,6,8,4]

list2 = [0,0,0,0,0]
print(list2+list)
'''

# +++++++++ Slicing +++++++++
# [start : end : step]
'''
list = [1,2,3,4,5,6,7,8]
print(list[:]) # reverse the list
Ṇ
b = [x*x for x in list]
print(b)
'''

# +++++++++ Tuple +++++++++

'''
t = ('a','p','p','l','e')
# print(t.index("p"))

my_tuple = [0,1,2,3,4,5,6,7]
a,*b,c,z = my_tuple
b.append(9)
print(a)
print(z)
print(b)
print(c)
'''

import sys
t = ['a','p','p','l','e']
t2 = ('a','p','p','l','e')
t3 = (6,9,1,7,4)

print(t3)

print(sys.getsizeof(t))
print(sys.getsizeof(t2))