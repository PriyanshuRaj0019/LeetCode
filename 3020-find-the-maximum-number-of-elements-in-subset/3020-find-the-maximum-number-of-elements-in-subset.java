import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maximumLength(int[] nums) {
        Map<Long, Integer> countMap = new HashMap<>();
        for (int num : nums) {
            countMap.put((long) num, countMap.getOrDefault((long) num, 0) + 1);
        }

        int maxLength = 1; // Any single element itself is a valid subset of length 1

        // 1. Handle the special case for 1
        if (countMap.containsKey(1L)) {
            int onesCount = countMap.get(1L);
            if (onesCount % 2 == 0) {
                maxLength = Math.max(maxLength, onesCount - 1);
            } else {
                maxLength = Math.max(maxLength, onesCount);
            }
        }

        // 2. Handle numbers > 1
        for (long key : countMap.keySet()) {
            if (key == 1) continue;

            int currentLength = 0;
            long currentNum = key;

            // Build the chain of squares
            while (countMap.containsKey(currentNum) && countMap.get(currentNum) >= 2) {
                currentLength += 2;
                currentNum = currentNum * currentNum; // Square it for the next step
            }

            // Check if the current number can act as the peak (must exist at least once)
            if (countMap.containsKey(currentNum)) {
                currentLength += 1;
            } else {
                // If it doesn't exist, the last element we counted had to be the peak instead.
                // Since we added 2 for it in the loop, we subtract 1 to make it a peak.
                currentLength -= 1;
            }

            maxLength = Math.max(maxLength, currentLength);
        }

        return maxLength;
    }
}