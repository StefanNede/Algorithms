public class Searching {
    public static void main(String[] args) {
        int[] arr = {2,3,4,5,6,7,8};
        int target = 6;
        System.out.println(linearSearch(arr, target));
        System.out.println(binarySearch(arr, target));
        System.out.println(sentinelSearch(arr, target));
    }

    public static int linearSearch(int[] arr, int target) {
        for (int i=0;i<arr.length;i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }

    public static int binarySearch(int[] arr, int target) {
        int lower = 0;
        int higher = arr.length-1;
        while (lower <= higher) {
            int median = Math.floorDiv(lower+higher,2);
            if (arr[median] == target) {
                return median;
            } else if (arr[median] > target) {
                higher = median-1;
            } else {
                lower = median+1;
            }
        }
        return -1;
    }
    
    public static int sentinelSearch(int[] arr, int target) {
        return -1;
    }
}