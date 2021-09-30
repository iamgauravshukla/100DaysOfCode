import numpy as np

array = np.array([[11,10,20,3],
                  [12,13,14,11],
                  [23,32,22,35],
                  [2,3,4,5]])
print(array)
newArrayRow = np.insert(array, 0, [[1,2,3,4]], axis= 0) # adding to row use axis = 0
newArrayCol = np.insert(array, 0, [[1,2,3,4]], axis= 1) # adding to coulmn use axis = 0
# print(newArrayRow)
# print(newArrayCol)

# Another method
newAppendArray = np.append(array, [[1,2,3,4]], axis= 0)
print(newAppendArray)