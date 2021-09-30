from array import *


def access(array, index):
    if index > (len(array) - 1):
        print('Index is not present in array')
    else:
        print(array[index])


numArray = array('i', [1, 2, 3, 4, 5, 6, 7])

access(numArray, 7)
