"""
Game of Life

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

 

Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 25
    board[i][j] is 0 or 1.

 

Follow up:

    Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
    In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
"""

# approach: iterative
# memory: O(n)
# runtime: O(n)
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # initialize queue
        queue = []
        
        # populate queue
        for i in range(len(board)):
            for j in range(len(board[i])):        
                # check surrounding cells
                surrounding_count = self.check_surroundings(board, i, j)                
                # any live cell
                if board[i][j] == 1:
                    # with fewer than two live neighbors dies
                    if surrounding_count < 2:
                        queue.append(0)
                    # with two or three live neighbors lives
                    if 2 <= surrounding_count <= 3:
                        queue.append(1)
                    # with more than three live neighbors dies
                    if surrounding_count > 3:
                        queue.append(0)
                # any dead cell
                if (board[i][j] == 0):
                    # with exactly three live neighbors becomes a live cell
                    if surrounding_count == 3:
                        queue.append(1)
                    else:
                        queue.append(0)
          
        # print(f"[DEBUG] queue: {queue}")
        # apply queue
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = queue.pop(0)

    def check_surroundings(self, board: List[List[int]], row: int, column: int) -> int:
        # initialize count
        count = 0
        
        # check top
        if row != 0:
            count += board[row - 1][column]
            # check top left
            if column != 0:
                count += board[row - 1][column - 1]
            # check top right
            if column != len(board[row]) - 1:
                count += board[row - 1][column + 1]
        # check bottom
        if row != len(board) - 1:
            count += board[row + 1][column]
            # check bottom left
            if column != 0:
                count += board[row + 1][column - 1]
            # check bottom right
            if column != len(board[row]) - 1:
                count += board[row + 1][column + 1]
        # check left
        if column != 0:
            count += board[row][column - 1]
        # check right
        if column != len(board[row]) - 1:
            count += board[row][column + 1]
            
        return count