"""
Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

 

Constraints:

    board and word consists only of lowercase and uppercase English letters.
    1 <= board.length <= 200
    1 <= board[i].length <= 200
    1 <= word.length <= 10^3
"""

# approach: brute force
# memory: O(m * n)
# runtime: O(m * n * 4^(l - 1)) m: rows, n: cols, l: word length
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        import copy
        self.board = board
        self.found = False
        self.word = word
        self.rows = len(board)
        self.cols = len(board[0])

        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] == word[0]:
                    if self.findNextLetter([], 1, i, j):
                        return True

        return False


    def findNextLetter(self, visited: List[tuple], index: int, row: int, col: int):
        char = ''
        vc = copy.deepcopy(visited) + [(row, col)]
        if index == len(self.word):
            return True
        else:
            char = self.word[index]

        # check up
        if row - 1 >= 0 and (row - 1, col) not in vc:
            if self.board[row - 1][col] == char:
                if self.findNextLetter(vc, index + 1, row - 1, col):
                    return True
                else:
                    pass

        # check right
        if col + 1 < self.cols and (row, col + 1) not in vc:
            if self.board[row][col + 1] == char:
                if self.findNextLetter(vc, index + 1, row, col + 1):
                    return True
                else:
                    pass

        # check down
        if row + 1 < self.rows and (row + 1, col) not in vc:
            if self.board[row + 1][col] == char:
                if self.findNextLetter(vc, index + 1, row + 1, col):
                    return True
                else:
                    pass

        # check left
        if col - 1 >= 0 and (row, col - 1) not in vc:
            if self.board[row][col - 1] == char:
                if self.findNextLetter(vc, index + 1, row, col - 1):
                    return True
                else:
                    pass
