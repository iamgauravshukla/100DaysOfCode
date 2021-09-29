tupOdd = (1, 3, 5, 7)
tupEven = (2, 4, 6, 8)

# tuple concatenate
print(tupOdd + tupEven)

# * for repetition
print(tupOdd * 2)

# in operator
print(1 in tupEven)

# count()
print(tupEven.count(2))

# index method
print(tupOdd.index(5))

# len function
print(len(tupOdd))

# max and min
print(max(tupOdd))
print(min(tupOdd))

# tuple method converts list into tuple
convertedTup = tuple([1, 2, 3, 4, 5])
print(convertedTup)