import random
def bubbleSort(arr):
    '''
    worst
    time complexity - O(n^2) worst case, O(n) best case, O(n^2) average case
    space complexity - O(1) 
    optimised with swapped flag
    '''
    end = len(arr)
    swapped = True
    while end > 0 and swapped:
        swapped = False
        for i in range(end-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        end -= 1
    return arr

def mergeSort(arr):
    '''
    fastest on average
    time complexity - O(nlogn) best case, O(nlogn) worst case, O(nlogn) average case
    space complexity - O(n)
    better than bubble sort and insertion sort for arrays that are further from sorted
    divide and conquer
    '''
    if len(arr) == 1:
        return arr
    
    # divide
    leftHalf = arr[:len(arr)//2]
    rightHalf = arr[len(arr)//2:]

    # conquer
    mergeSort(leftHalf)
    mergeSort(rightHalf)

    # merge
    leftPointer = 0
    rightPointer = 0
    resPointer = 0
    
    while leftPointer < len(leftHalf) and rightPointer < len(rightHalf):
        if leftHalf[leftPointer] < rightHalf[rightPointer]:
            arr[resPointer] = leftHalf[leftPointer]
            leftPointer += 1
            resPointer += 1
        else:
            arr[resPointer] = rightHalf[rightPointer]
            rightPointer += 1
            resPointer += 1
    
    while leftPointer < len(leftHalf):
        arr[resPointer] = leftHalf[leftPointer]
        leftPointer += 1
        resPointer += 1

    while rightPointer < len(rightHalf):
        arr[resPointer] = rightHalf[rightPointer]
        rightPointer += 1
        resPointer += 1

    return arr

def insertionSort(arr):
    '''
    time complexity - O(n^2) worst case, O(n) best case, O(n^2) average case
    space complexity - O(1)
    better than bubble sort, worse than merge for arrays that are further from sorting
    '''
    for i in range(1, len(arr)):
        el = arr[i]
        # place it in the right place - go backwards through sorted part and swap it 
        for j in range(i-1, -1, -1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i -= 1
            else:
                break
    return arr

def quickSort(arr):
    '''
    2nd fastest on average
    unstable 
    time complexity - O(n^2) worst case, O(nlogn) best case, O(nlogn) average case
    space complexity - O(n^2) worst case, O(n) best case, O(n) average case
    '''
    if len(arr) <= 1:
        return arr
    # use middle value as pivot 
    pivot = arr[len(arr)//2]
    leftHalf = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    rightHalf = [x for x in arr if x > pivot]

    return quickSort(leftHalf) + middle + quickSort(rightHalf)

def quickSort2(arr):
    '''
    sorts in place
    unstable
    time complexity - O(n^2) worst case, O(nlogn) best and average case
    space complexity - O(n) worst case, O(logn) best and average case
    '''
    def partition(lowerP, higherP, pivotP):
        arr[lowerP], arr[pivotP] = arr[pivotP], arr[lowerP]

        pivotEl = arr[lowerP]
        smallerIndex = lowerP+1

        for largerIndex in range(lowerP+1, higherP+1):
            if arr[largerIndex] < pivotEl:
                arr[smallerIndex], arr[largerIndex] = arr[largerIndex], arr[smallerIndex]
                smallerIndex += 1
        
        # place pivot back in the right place
        pivotP = smallerIndex - 1
        arr[lowerP], arr[pivotP] = arr[pivotP], arr[lowerP]

        return pivotP

    def qSort(lowerP, higherP):
        if lowerP >= higherP: return 
        pivotP = random.randint(lowerP, higherP)

        pivotP = partition(lowerP, higherP, pivotP)

        qSort(lowerP, pivotP-1)
        qSort(pivotP+1, higherP)

        return 

    qSort(0, len(arr)-1)
    return arr

test = [27, 72, 45, 42, 87, 64, 98, 88, 85, 33, 69, 66, 44, 91, 76, 80, 59, 7, 45, 100, 34, 5, 22, 43, 31, 34, 86, 45, 31, 77, 31, 71, 99, 39, 40, 22, 68, 20, 92, 81, 30, 73, 3, 78, 46, 24, 81, 67, 79, 51, 99, 6, 5, 17, 15, 98, 43, 32, 64, 53, 41, 64, 92, 74, 12, 5, 94, 62, 84, 59, 76, 21, 9, 97, 85, 41, 43, 32, 15, 84, 44, 3, 59, 45, 82, 90, 13, 1, 95, 62, 71, 22, 98, 77, 67, 10, 9, 97, 1, 93]
# print(bubbleSort(test))
# print(mergeSort(test))
# print(insertionSort(test))
# print(quickSort(test))
print(quickSort2(test))