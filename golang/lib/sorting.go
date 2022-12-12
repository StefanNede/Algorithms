package algorithms

import "fmt"

func BubbleSort(arr []int) []int {
	endIndex := len(arr)
	for endIndex >= 0 {
		for i := 0; i < endIndex-1; i++ {
			if arr[i] > arr[i+1] {
				temp := arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = temp
			}
		}
		endIndex--
	}
	return arr
}

func InsertionSort(arr []int) []int {
	for i := 1; i < len(arr); i++ {
		for j := i - 1; j > -1; j-- {
			if arr[i] < arr[j] {
				temp := arr[i]
				arr[i] = arr[j]
				arr[j] = temp
				i--
			} else {
				break
			}
		}
	}
	return arr
}

func MergeSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	// divide
	midPoint := len(arr) / 2
	leftHalf := arr[:midPoint] // some fuckery is happening with these arrays
	rightHalf := arr[midPoint:]

	// conquer
	sortedLeftHalf := MergeSort(leftHalf)
	sortedRightHalf := MergeSort(rightHalf)

	// merge
	leftPointer := 0
	rightPointer := 0
	resPointer := 0

	for (leftPointer < len(sortedLeftHalf)) && (rightPointer < len(sortedRightHalf)) {
		if sortedLeftHalf[leftPointer] < sortedRightHalf[rightPointer] {
			arr[resPointer] = sortedLeftHalf[leftPointer]
			leftPointer++
		} else {
			fmt.Println(arr, sortedRightHalf[rightPointer])
			arr[resPointer] = sortedRightHalf[rightPointer]
			rightPointer++
		}
		resPointer++
	}

	for leftPointer < len(sortedLeftHalf) {
		arr[resPointer] = sortedLeftHalf[leftPointer]
		leftPointer++
		resPointer++
	}

	for rightPointer < len(sortedRightHalf) {
		arr[resPointer] = sortedRightHalf[rightPointer]
		rightPointer++
		resPointer++
	}

	return arr
}

func QuickSort(arr []int) []int {
	var partition func(int, int, int) int
	partition = func(lowerIndex, higherIndex, pivotIndex int) int {
		temp := arr[lowerIndex]
		arr[lowerIndex] = arr[pivotIndex]
		arr[pivotIndex] = temp

		pivot := arr[lowerIndex]
		smallerIndex := lowerIndex + 1
		for largerIndex := lowerIndex + 1; largerIndex < higherIndex+1; largerIndex++ {
			if arr[largerIndex] < pivot {
				temp = arr[smallerIndex]
				arr[smallerIndex] = arr[largerIndex]
				arr[largerIndex] = temp
				smallerIndex++
			}
		}

		// re-insert pivot in the right place
		pivotIndex = smallerIndex - 1
		temp = arr[lowerIndex]
		arr[lowerIndex] = arr[pivotIndex]
		arr[pivotIndex] = temp

		return pivotIndex
	}

	var qSort func(int, int)
	qSort = func(lowerIndex, higherIndex int) {
		if lowerIndex >= higherIndex {
			return
		}

		pivotIndex := (lowerIndex + higherIndex) / 2
		pivotIndex = partition(lowerIndex, higherIndex, pivotIndex)

		// recursively run quick sort on left and right side of partition
		qSort(lowerIndex, pivotIndex-1)
		qSort(pivotIndex+1, higherIndex)

		return
	}
	qSort(0, len(arr)-1)
	return arr
}
