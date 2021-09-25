from array import *


def searchArray(arrays, value):
    for i in arrays:
        if i == value:
            return value, 'present at', arrays.index(i)
    return "Element not exists in array"


numArray = array('i',[11, 22, 33, 54, 95, 66, 78, 80])
print(searchArray(numArray, 66))
