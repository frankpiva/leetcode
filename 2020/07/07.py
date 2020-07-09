"""
Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
"""

# approach: small brain iterate and calculate
# memory: O(n)
# runtime: O(n)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        # short circuit case: [[]]
        if grid == [[]]: return 0

        # everything else
        self.grid = grid
        self.x = len(grid[0])
        self.y = len(grid)
        perimeter = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4 - self.numberOfNeighbors(i,j)
        return perimeter


    def numberOfNeighbors(self, y: int, x: int) -> int:
        neighbors = 0
        if x != 0:
            neighbors += self.grid[y][x-1]
        if x < self.x - 1:
            neighbors += self.grid[y][x+1]
        if y != 0:
            neighbors += self.grid[y-1][x]
        if y < self.y - 1:
            neighbors += self.grid[y+1][x]
        return neighbors


# approach: big brain iterate and calculate
# memory: O(n)
# runtime: O(n)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        # short circuit case: [[]]
        if grid == [[]]: return 0

        # everything else
        cols = len(grid[0])
        rows = len(grid)
        perimeter = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i != 0:
                        perimeter -= grid[i-1][j]
                    if i < rows - 1:
                        perimeter -= grid[i+1][j]
                    if j != 0:
                        perimeter -= grid[i][j-1]
                    if j < cols - 1:
                        perimeter -= grid[i][j+1]

        return perimeter
