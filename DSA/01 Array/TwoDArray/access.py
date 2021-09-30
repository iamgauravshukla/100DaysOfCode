import numpy as np

array = np.array([[11,10,20,3],
                  [12,13,14,11],
                  [23,32,22,35]])

def access(arr, rowIndex, colIndex):
    if rowIndex >= len(arr) or colIndex>= len(arr[0]):
        print('Incorrect Index')
    else:
        print(arr[rowIndex][colIndex])

access(array,1,3)

