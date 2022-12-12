import java.util.Arrays;

public class Sorting {
    public static void main(String[] args) {
        int[] arr = {9,4,5,7,2,1,4,7,9,5,2,7,214,12,100};
        System.out.println(Arrays.toString(bubbleSort(arr)));
        System.out.println(Arrays.toString(insertionSort(arr)));
        System.out.println(Arrays.toString(mergeSort(arr)));
        System.out.println(Arrays.toString(quickSort(arr)));
    }

    public static int[] bubbleSort(int[] arr) {
        int last = arr.length-1;
        boolean swapsMade = true;
        while (last > 0 && swapsMade) {
            swapsMade = false;
            for (int i = 0; i < last; i++) {
                if (arr[i] > arr[i+1]) {
                    int temp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = temp;
                    swapsMade = true;
                }
            }
            last--;
        }
        return arr;
    }

    public static int[] insertionSort(int[] arr) {
        for (int i=0; i < arr.length; i++) {
            int indexItemToRemove = i;
            int itemToRemove = arr[indexItemToRemove];
            while (indexItemToRemove > 0 && arr[indexItemToRemove-1] > itemToRemove) {
                int temp = arr[indexItemToRemove];
                arr[indexItemToRemove] = arr[indexItemToRemove-1];
                arr[indexItemToRemove-1] = temp;
                indexItemToRemove--;
            }
            arr[indexItemToRemove] = itemToRemove;
        }
        return arr;
    }

    public static int[] mergeSort(int[] arr) {
        if (arr.length <= 1) {
            return arr;
        }
        
        // divide
        int median = Math.floorDiv(arr.length, 2);
        int[] leftHalf = Arrays.copyOfRange(arr, 0, median);
        int[] rightHalf = Arrays.copyOfRange(arr, median, arr.length);

        // conquer
        leftHalf = mergeSort(leftHalf);
        rightHalf = mergeSort(rightHalf);

        // merge
        int leftIndex = 0;
        int rightIndex = 0;
        int resIndex = 0;
        
        while (leftIndex < leftHalf.length && rightIndex < rightHalf.length) {
            if (leftHalf[leftIndex] < rightHalf[rightIndex]) {
                arr[resIndex] = leftHalf[leftIndex];
                leftIndex++;
            } else {
                arr[resIndex] = rightHalf[rightIndex];
                rightIndex++;
            }
            resIndex++;
        }

        while (leftIndex < leftHalf.length) {
            arr[resIndex] = leftHalf[leftIndex];
            leftIndex++;
            resIndex++;
        }

        while (rightIndex < rightHalf.length) {
            arr[resIndex] = rightHalf[rightIndex];
            rightIndex++;
            resIndex++;
        }
        
        return arr;
    }

    public static int[] quickSort(int[] arr) {
        arr = sort(arr, 0, arr.length-1);
        return arr;
    }
    
    private static int[] sort(int arr[], int low, int high)
    {
        if (low < high)
        {
            /* pi is partitioning index, arr[pi] is
              now at right place */
            int pi = partition(arr, low, high);
 
            // Recursively sort elements before
            // partition and after partition
            sort(arr, low, pi-1);
            sort(arr, pi+1, high);
            return arr;
        }
        return arr;
    }

    private static int partition(int arr[], int low, int high)
    {
        int pivot = arr[high];
        int i = (low-1); // index of smaller element
        for (int j=low; j<high; j++)
        {
            // If current element is smaller than or
            // equal to pivot
            if (arr[j] <= pivot)
            {
                i++;
 
                // swap arr[i] and arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
 
        // swap arr[i+1] and arr[high] (or pivot)
        int temp = arr[i+1];
        arr[i+1] = arr[high];
        arr[high] = temp;
 
        return i+1;
    }
}
