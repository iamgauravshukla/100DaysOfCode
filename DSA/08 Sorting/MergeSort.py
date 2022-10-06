def merge(customList, l, m, r):
    # l = left (initial) , m = middle, r = right (last)
    n1 = m - l+1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = customList[l+i]

    for j in range(0, n2):
        R[j] = customList[m+1+j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]