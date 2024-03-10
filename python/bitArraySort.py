def bitArraySort(arr):
    i = 0
    j = len(arr)-1
    while i < j:
        while arr[i] == 0:
            i += 1
        while arr[j] == 1:
            j -= 1
        print(i,j)
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    return arr


print(bitArraySort([0,1,1,0,0,0,1,0]))

