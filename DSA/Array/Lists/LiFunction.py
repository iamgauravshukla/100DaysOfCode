# +
a = [1, 2, 3]
b = [4, 5, 6, 7]
c = a + b
print(c)

# * makes elements repeated
d = [1, 2]
print(d*3)

# Length
print(len(b))

# Max num and min num
print(max(b))
print(min(b))

# sum method
print(sum(b))

# String and Lists
a = "gaurav"
b = list(a)
print(b)

# split
phrase = "Hey Hey Hey Hey"
wordList = phrase.split(" ") # space is delimiter here
print(wordList)

# join
listToPhrase = "-".join(wordList) # Here "-" is delimiter to join the list
print(listToPhrase)

# sort
numList = [9, 7, 5, 2, 10]
sortedList = numList[:]
sortedList.sort()
print(sortedList)