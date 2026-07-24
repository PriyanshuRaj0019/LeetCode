class Solution {
    public int uniqueXorTriplets(int[] nums) {
        // Max value is 1500, which is < 2048 (11 bits). 
        // Max possible XOR of any numbers <= 1500 is 2047.
        int MAX_XOR = 2048; 
        
        // Step 1: Find unique elements
        boolean[] hasNum = new boolean[MAX_XOR];
        for (int num : nums) {
            hasNum[num] = true;
        }
        
        // Step 2: Generate all pairwise XOR values
        boolean[] s2 = new boolean[MAX_XOR];
        for (int i = 0; i < MAX_XOR; i++) {
            if (hasNum[i]) {
                for (int j = 0; j < MAX_XOR; j++) {
                    if (hasNum[j]) {
                        s2[i ^ j] = true;
                    }
                }
            }
        }
        
        // Step 3: Generate triplet XOR values and count unique results
        boolean[] s3 = new boolean[MAX_XOR];
        int count = 0;
        
        for (int i = 0; i < MAX_XOR; i++) {
            if (s2[i]) {
                for (int j = 0; j < MAX_XOR; j++) {
                    if (hasNum[j]) {
                        int xorSum = i ^ j;
                        // If we haven't seen this triplet sum yet, count it
                        if (!s3[xorSum]) {
                            s3[xorSum] = true;
                            count++;
                        }
                    }
                }
            }
        }
        
        return count;
    }
}