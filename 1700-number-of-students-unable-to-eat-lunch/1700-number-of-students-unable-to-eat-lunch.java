class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        int[] counts = new int[2]; // counts[0] for circular, counts[1] for square
        
        // Count the preferences of all students
        for (int student : students) {
            counts[student]++;
        }
        
        // Serve the sandwiches one by one
        for (int sandwich : sandwiches) {
            // If no student wants the current top sandwich, the line stalls
            if (counts[sandwich] == 0) {
                break;
            }
            // A student takes the sandwich
            counts[sandwich]--;
        }
        
        // The number of remaining students is the sum of leftover preferences
        return counts[0] + counts[1];
    }
}