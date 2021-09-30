# Find the maximum product of two integers in the array where all elements are positive integer
import numpy as np

intArray = np.array([2, 12, 8, 13, 11, 17, 19, 21, 24, 31, 28, 41, 26, 32])

def maxProduct(array):
    maxPro = 0
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] * array[j] > maxPro:
                maxPro = array[i] * array[j]
                pairs = str(array[i]) + "*" + str(array[j])
    print(pairs)
    print(maxPro)

maxProduct(intArray)