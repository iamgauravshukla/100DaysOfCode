newTuple = 'a', 'b', 'c', 'd'
print(type(newTuple))

# best practice to add ()
another = ('a', 'b', 'c')
print(type(another))

# tuple with single element
singleton = ('a',)
print(type(singleton))

# creating empty tuple
emptyTuple = tuple()
print(type(emptyTuple))

# tuple treat each characters as separate element
tupleString = tuple('abed')
print(tupleString)
