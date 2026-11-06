class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # Initialize an m x n grid filled with obstacles '#'
        grid = [["#"] * n for _ in range(m)]
        
        # Path: Go right across the top row (row 0)
        for j in range(n):
            grid[0][j] = "."
            
        # Path: Go down the last column (column n - 1)
        for i in range(m):
            grid[i][n - 1] = "."
            
        # Convert each row into a string
        return ["".join(row) for row in grid]