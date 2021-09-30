# Check if array contain an number in python
import numpy as np

intArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
# search 10 in array

def search(array, n):
    for i in range(0, len(array)):
        if array[i] == n:
            return "Element found at index", i
    return "Element not found"

print(search(intArray, 10))


