import numpy as np

numArray = np.array([[11,10,20,3],
                  [12,13,14,11],
                  [23,32,22,35],])

def traverse(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverse(numArray)