# Check if a list has all unique characters

numList = [1, 23, 32, 44, 51, 20, 10, 13, 17, 19, 21, 24, 25, 2, 45, 5, 6, 98, 100]
uniList = []

def unique(array):
    for element in array:
        if element in uniList:
            return False
        else:
            uniList.append(element)
    return True

print(unique(numList))