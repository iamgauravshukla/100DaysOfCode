# To find the all pair of numbers whose sum is equal to a given number : Ex n = 9 , pair [6,3] [9,0] [1,8] ...
from array import *
numArray = array('i', [0, 2, 5, 8, 6, 1, 7, 4, 4, 6])
n = 8
pair = []
for i in range(0,len(numArray)):
    for j in range(1, len(numArray)):
        if numArray[i]+numArray[j] == n:
            if [numArray[i], numArray[j]] and [numArray[j], numArray[i]] not in pair:
                pair.append([numArray[i], numArray[j]])

print(pair)
