# Slicing
charList = ['g', 'a', 'u', 'r', 'a', 'v']
print([charList[0:2]])

# methods for deletion
print(charList.pop())  # Removes from end of the list
print(charList.pop(0))
print(charList)

# Delete method
del charList[2]
del charList[0:2]  # Also deletes multiple elements
print(charList)

# remove method
charList.remove('a')
print(charList)