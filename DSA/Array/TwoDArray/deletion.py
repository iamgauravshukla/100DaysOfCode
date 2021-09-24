import numpy as np

numArray = np.array([[2, 4, 6, 8],
                     [1, 3, 5, 7],
                    [10, 12, 14, 16]])

newArray = np.delete(numArray, 2, axis=0) # delete row axis=0
newArray = np.delete(numArray, 2, axis=1) # delete column axis = 0
print(newArray)
