def linearSearch(arr, target):
    '''
    time complexity - O(n) worst case, O(1) best case, O(n) average case
    space complexity - O(1)
    '''
    for i in range(len(arr)):
        if arr[i] == target: 
            return i 
    return -1

def binarySearch(arr, target):
    '''
    time complexity - O(logn) worst case, O(1) best case, O(logn) average case
    space complexity - O(1)
    however array must be sorted
    '''
    arr = sorted(arr)
    smallerP = 0
    largerP = len(arr)-1
    while smallerP <= largerP:
        medianP = (smallerP + largerP)//2
        if arr[medianP] == target:
            return medianP
        elif arr[medianP] > target:
            largerP = medianP-1
        else:
            smallerP = medianP+1
    return -1

def sentinelSearch(arr, target):
    '''
    time complexity - O(n) worst case, O(1) best case, O(n) average case
    space complexity - O(1)
    faster than linear search because it removes a check from each iteration to make sure it hasn't gone out of bounds of the list 
    '''
    arr.append(target)
    pos = 0
    while arr[pos] != target:
        pos += 1

    arr.pop(-1)
    if pos == len(arr):
        return -1
    else:
        return pos

arr = [27, 72, 45, 42, 87, 64, 98, 88, 85, 33, 69, 66, 44, 91, 76, 80, 59, 7, 45, 100, 34, 5, 22, 43, 31, 34, 86, 45, 31, 77, 31, 71, 99, 39, 40, 22, 68, 20, 92, 81, 30, 73, 3, 78, 46, 24, 81, 67, 79, 51, 99, 6, 5, 17, 15, 98, 43, 32, 64, 53, 41, 64, 92, 74, 12, 5, 94, 62, 84, 59, 76, 21, 9, 97, 85, 41, 43, 32, 15, 84, 44, 3, 59, 45, 82, 90, 13, 1, 95, 62, 71, 22, 98, 77, 67, 10, 9, 97, 1, 93]
target = 6
print(linearSearch(arr, target))
print(sentinelSearch(arr, target))
print(binarySearch(arr, target))