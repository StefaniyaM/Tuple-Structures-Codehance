# Tuple items are enclosed in round brackets
# Tuple is ordered
# Tuple is immutable
# Tuple elements do not need to be unique
# Elements can be of different data types

'''
Creating a Tuple
'''
# tuple = ()
# tuple = ('cat', [4, 3, 2, 1], (1, 2, 3))
# tuple = 1234, 4321
# tuple = "hello",
# tuple = ('hello',)
# print(tuple)

'''
Access Tuple Elements
'''

# tuple = (1234, 4321, 'hello')
# print(tuple[0])
# print(tuple[-1])
# print(tuple[-2])

'''
Slicing Tuples in Python
'''

# fruits = ('orange', 'apple', 'pear', 'grapes', 'banana')
# print(fruits[:])
# print(fruits[2:5])
# print(fruits[:-2])
# print(fruits[:2])
# print(fruits[2:])
# print(fruits[::2])
# print(fruits[::-1])

'''
Changing a Tuple
'''

# fruits = ('orange', 'apple', 'pear', 'grapes', 'banana')
# fruits[0] = 'pear'
# # which makes tuples faster and use less memory (runs faster) than a list


'''
Deleting a Tuple
'''

# fruits = ('orange', 'apple', 'pear', 'grapes', 'banana')
# del fruits[0]
# print(fruits)

# del fruits
# print(fruits)
#  we cannot change what is inside the tuple, but we can delete a tuple completely


'''
Tuple Methods
'''

# print(dir(tuple))
# print(dir(list))

# fruits = ('orange', 'apple', 'pear', 'grapes', 'orange', 'banana')
# print(fruits.count('orange'))
# print(fruits.index('apple'))

