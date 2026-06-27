import java.util.Stack;

class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();

        for (String token : tokens) {
            // Check if the token is an operator
            if (token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")) {
                // Pop operands in reverse order
                int b = stack.pop();
                int a = stack.pop();

                switch (token) {
                    case "+":
                        stack.push(a + b);
                        break;
                    case "-":
                        stack.push(a - b);
                        break;
                    case "*":
                        stack.push(a * b);
                        break;
                    case "/":
                        stack.push(a / b); // Java integer division naturally truncates toward zero
                        break;
                }
            } else {
                // Token is a valid 32-bit integer, parse and push it
                stack.push(Integer.parseInt(token));
            }
        }

        // The final remaining element is the result of the entire expression
        return stack.pop();
    }
}