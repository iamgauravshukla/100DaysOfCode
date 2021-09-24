import numpy as np

numArray = np.array([[2, 4, 6, 8],
                     [1, 3, 5, 7],
                    [10, 12, 14, 16]])

def search(array, value):
    for i in range(len(numArray)):
        for j in range(len(numArray[0])):
            if numArray[i][j] == value:
                return "Element Found at index " + str(i) +' '+ str(j)
    return "Element not found"

print(search(numArray, 1))
