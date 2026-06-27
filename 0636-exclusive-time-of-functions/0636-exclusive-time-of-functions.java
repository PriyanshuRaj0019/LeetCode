import java.util.List;
import java.util.Stack;

class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>();
        int prevTime = 0;

        for (String log : logs) {
            // Split the log string into component parts: "id:status:timestamp"
            String[] parts = log.split(":");
            int id = Integer.parseInt(parts[0]);
            String type = parts[1];
            int timestamp = Integer.parseInt(parts[2]);

            if (type.equals("start")) {
                // If there's an active function, attribute the elapsed time to it
                if (!stack.isEmpty()) {
                    result[stack.peek()] += timestamp - prevTime;
                }
                // Push the new function to the stack and update prevTime
                stack.push(id);
                prevTime = timestamp;
            } else {
                // The current function is ending. Add the execution time including this timestamp
                result[stack.peek()] += timestamp - prevTime + 1;
                // Remove it from the stack
                stack.pop();
                // Next active period starts at the beginning of the next time unit
                prevTime = timestamp + 1;
            }
        }

        return result;
    }
}