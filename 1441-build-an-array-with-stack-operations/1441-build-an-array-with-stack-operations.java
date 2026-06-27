import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> result = new ArrayList<>();
        int streamNum = 1; // Tracks the current number from the [1, n] stream
        
        for (int targetNum : target) {
            // While the stream hasn't reached the current target number,
            // we must simulate pushing and popping the numbers we want to skip.
            while (streamNum < targetNum) {
                result.add("Push");
                result.add("Pop");
                streamNum++;
            }
            
            // Now streamNum == targetNum, so we push it to keep it in the stack.
            result.add("Push");
            streamNum++;
        }
        
        return result;
    }
}