numList = [1, 3, 5, 7, 9, 11, 24]

# if 1 in numList:
#     print('Item present at ', numList.index(1), ' index')
# else:
#     print("Element doesn't exists")

def searchList(list, value):
    for i in list:
        if i == value:
            return 'Item present at index ', list.index(value)
    else:
        return "Item doesn't exist"

print(searchList(numList, 5))