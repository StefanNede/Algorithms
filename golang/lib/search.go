package algorithms

func LinearSearch(arr []int, target int) int {
	for i, el := range arr {
		if el == target {
			return i
		}
	}
	return -1
}

func BinarySearch(arr []int, target int) int {
	lowerPointer := 0
	higherPointer := len(arr) - 1
	for lowerPointer <= higherPointer {
		midPointer := (lowerPointer + higherPointer) / 2
		if arr[midPointer] == target {
			return midPointer
		} else if arr[midPointer] > target {
			higherPointer = midPointer - 1
		} else {
			lowerPointer = midPointer + 1
		}
	}
	return -1
}

func SentinelSearch(arr []int, target int) int {
	arr = append(arr, target)
	res := 0
	for arr[res] != target {
		res++
	}
	if res == len(arr) {
		res = -1
	}
	arr = arr[:len(arr)-1]
	return res
}
