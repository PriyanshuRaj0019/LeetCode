import java.util.Arrays;

class Solution {
    public int[] sortByBits(int[] arr) {
        // Encode both the bit count and the original value into the same number
        for (int i = 0; i < arr.length; i++) {
            arr[i] += Integer.bitCount(arr[i]) * 10001;
        }
        
        // Sort the array in ascending order
        // The bit count naturally takes priority because of the 10001 multiplier
        Arrays.sort(arr);
        
        // Decode the values back to their original form
        for (int i = 0; i < arr.length; i++) {
            arr[i] %= 10001;
        }
        
        return arr;
    }
}