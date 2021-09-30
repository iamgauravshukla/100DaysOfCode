# Missing Number
# Find the missing number in the integer array between 1 to n
# Formula used 👇
# 1 + 2 + 3 + ...+ n = n(n+1)/2 = Sum of the series

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Size on numList array = n

def missing(list, n):
    sumNum = n*(n+1)/2
    sumList = sum(list)
    missingNum = sumNum - sumList
    return "Missing Number is " + str(missingNum)

print(missing(numList, 20))