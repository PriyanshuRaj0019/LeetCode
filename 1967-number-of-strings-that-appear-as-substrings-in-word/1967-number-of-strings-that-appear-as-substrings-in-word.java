class Solution {
    public int numOfStrings(String[] patterns, String word) {
        int matchCount = 0;
        
        // Check each pattern string against the target word
        for (String pattern : patterns) {
            if (word.contains(pattern)) {
                matchCount++;
            }
        }
        
        return matchCount;
    }
}