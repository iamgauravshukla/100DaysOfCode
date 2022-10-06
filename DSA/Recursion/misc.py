# Reverse and word using recursion
"""
words = 'killer'

def revWord(word):
    if len(word) <= 1:
        return word
    return word[len(word) - 1] + revWord(word[0:len(word) - 1])

print(revWord(words))

"""

"""
strngV = 'levesl'


def isPalindrome(strng):
    if len(strng) <= 1:
        return True
    if strng[0] != strng[len(strng) - 1]:
        return False
    return isPalindrome(strng[1:-1])

print(isPalindrome(strngV))

"""

"""
# IsOdd

arr = [4, 6, 8, 10]

def someRecursive(array, fun):
    if len(array) == 0:
        return False
    if not(fun(array[0])):
        return someRecursive(array[1:], fun)
    return True


def IsOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True

print(someRecursive(arr, IsOdd))

"""

#flatten
"""
arr = [[[1]], [[[2]]], [[[[[[[[3]]]]]]]]]

def flatten(array):
    result = []
    for i in array:
        if type(i) is list:
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

print(flatten(arr))
"""

arrL = ['cow', 'mow', 'chow', 'pau']

def CapitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].capitalize())
    return result + CapitalizeFirst(arr[1:])

print(CapitalizeFirst(arrL))