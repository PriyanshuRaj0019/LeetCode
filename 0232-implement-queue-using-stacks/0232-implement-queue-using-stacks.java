import java.util.Stack;

class MyQueue {
    private Stack<Integer> input;
    private Stack<Integer> output;

    public MyQueue() {
        input = new Stack<>();
        output = new Stack<>();
    }
    
    // Push element x to the back of the queue.
    public void push(int x) {
        input.push(x);
    }
    
    // Removes the element from the front of the queue and returns it.
    public int pop() {
        peek(); // Ensures output stack has the current elements in FIFO order
        return output.pop();
    }
    
    // Get the front element.
    public int peek() {
        // If output stack is empty, move all elements from input to output
        if (output.isEmpty()) {
            while (!input.isEmpty()) {
                output.push(input.pop());
            }
        }
        return output.peek();
    }
    
    // Returns whether the queue is empty.
    public boolean empty() {
        return input.isEmpty() && output.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */