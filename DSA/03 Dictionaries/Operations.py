# Dictionary Operations
dictionary = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

# key in dictionary
print(2 in dictionary)  # Returns true/false
if 1 in dictionary:
    print(dictionary[1])

# for values
print('one' in dictionary.values())

# for in dictionary to traversal  : Time complexity O(n)
for key in dictionary:
    print(key, dictionary[key])

# len()
print(len(dictionary))  # Returns number of pairs

# sorted() method
vowels = {'e': 1, 'i': 2, 'o': 3, 'a': 4, 'u': 5}
random = {'were': 1, 'hi': 2, 'loa': 3, 'answer': 4, 'uno': 5}
sortedVowels = sorted(vowels, reverse=False)
randomSorted = sorted(random, key=len)  # returns sorted list based on key
print(sortedVowels)
print(randomSorted)



