def bitArraySort(arr):
    i = 0
    j = len(arr)-1
    while i < j:
        while arr[i] == 0:
            i += 1
        while arr[j] == 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    return arr


print(bitArraySort([0,1,1,0,0,0,1,0]))

# Given a sorted array of integers and a target value, determine if there exists two integers
# in the array that sum up to the target value.
def findNumInArr(arr, num):
    for i in arr:
        diff = num-i
        if diff in arr:
            return True
    return False


def findNumInArr2(arr, num):
    i = 0
    j = len(arr)-1
    while(i < j):
        if arr[i] + arr[j] == num:
            return True;
        elif arr[i] + arr[j] < num:
            i += 1
        else:
            j -= 1
    return False

print(findNumInArr2([12, 13, 15, 32, 37, 50, 57, 66, 79, 80], 82))
print(findNumInArr2([12, 13, 15, 32, 37, 50, 57, 67, 79, 80], 81))

#find index of number
def binarySearch(arr, num):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid =(end+start)//2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            start = mid+1
        else:
            end = mid-1
    return -1

print(binarySearch([1, 22, 33, 45, 56, 59, 71, 74, 77, 82], 77))
print(binarySearch([1, 22, 33, 45, 56, 59, 71, 74, 77, 82], 98))
print(binarySearch([1, 22, 33, 45, 56, 59, 71, 74, 77, 82], 60))

#prime factor - euclid's algorithm
def euclid(a,b):
    if b > a:
        a,b = b,a
    while b is not 0:
        tmp = b
        b = a % b
        if b != 0:
            a = b
    return a

print(euclid(78, 52))

