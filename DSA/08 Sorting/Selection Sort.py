def selectionSort(customList):
    for i in range(len(customList)):
        minIndex = i
        for j in range(i+1, len(customList)):
            if customList[minIndex] > customList[j]:
                minIndex = j
        customList[i], customList[minIndex] = customList[minIndex], customList[i]
    print(customList)


cList = [2, 5, 7, 3, 1, 9, 8]
selectionSort(cList)