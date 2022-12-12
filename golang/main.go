package main

import (
	S "algorithms/lib"
	"fmt"
)

func main() {
	// searching
	arr := []int{1, 2, 3, 5, 6}
	target := 5
	fmt.Println(S.LinearSearch(arr, target))
	fmt.Println(S.BinarySearch(arr, target))
	fmt.Println(S.SentinelSearch(arr, target))

	// sorting
	arr = []int{27, 72, 45, 42, 87, 64, 98, 88, 85, 33, 69, 66, 44, 91, 76, 80, 59, 7, 45, 100, 34, 5, 22, 43, 31, 34, 86, 45, 31, 77, 31, 71, 99, 39, 40, 22, 68, 20, 92, 81, 30, 73, 3, 78, 46, 24, 81, 67, 79, 51, 99, 6, 5, 17, 15, 98, 43, 32, 64, 53, 41, 64, 92, 74, 12, 5, 94, 62, 84, 59, 76, 21, 9, 97, 85, 41, 43, 32, 15, 84, 44, 3, 59, 45, 82, 90, 13, 1, 95, 62, 71, 22, 98, 77, 67, 10, 9, 97, 1, 93}
	fmt.Println(S.BubbleSort(arr))
	fmt.Println(S.InsertionSort(arr))
	// fmt.Println(S.MergeSort(arr))
	fmt.Println(S.QuickSort(arr))
}
