"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

 

Note:

    All inputs are consist of lowercase letters a-z.
    The values of words are distinct.
"""

# approach: backtracking, passes 34/36 tests
# memory: exponential
# runtime: exponential
import copy

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        print(len(board), len(board[0]))
        self.board = board
        self.length = len(board)
        self.width = len(board[0])
        self.matches = []
        self.bigs = []
        
        for word in words:
            for i in range(0, self.length):
                for j in range(0, self.width):
                    if board[i][j] == word[0]:
                        # print('first letter found', i, j)
                        # start checking adjacent cells
                        # self.checkCandidate(word, 0, i, j, [])   
                        if self.checkCandidate(word, 0, i, j, {}): break   
        return list(dict.fromkeys(self.matches))
                        
    def checkCandidate(self, word, index, row, col, cv):
        cvCopy = copy.deepcopy(cv)
        # check the next character
        if index + 1 < len(word):
            index += 1
        # we finished checking the word
        else:
            self.matches.append(word)
            return True
            
        nextChar = word[index]
        
        # don't check cells that we came from, search clockwise
        if not cvCopy.get((row, col + 1)): # right
            if self.checkRightCell(nextChar, row, col):
                cvCopy[(row, col)] = True
                self.checkCandidate(word, index, row, col+1, cvCopy)
                
        if not cvCopy.get((row+1, col)): # below
            if self.checkBelowCell(nextChar, row, col):
                cvCopy[(row, col)] = True
                self.checkCandidate(word, index, row+1, col, cvCopy)
                
        if not cvCopy.get((row, col-1)): # left
            if self.checkLeftCell(nextChar, row, col):
                cvCopy[(row, col)] = True
                self.checkCandidate(word, index, row, col-1, cvCopy)
                
        if not cvCopy.get((row-1, col)): # above
            if self.checkAboveCell(nextChar, row, col):
                cvCopy[(row, col)] = True
                self.checkCandidate(word, index, row-1, col, cvCopy)
        
    def checkAboveCell(self, char, row, col):
        if row - 1 >= 0:
            if self.board[row - 1][col] == char:
                return True
        return False
    
    def checkBelowCell(self, char, row, col):
        if row + 1 < self.length:
            if self.board[row + 1][col] == char:
                return True
        return False
        
    def checkLeftCell(self, char, row, col):
        if col - 1 >= 0:
            if self.board[row][col - 1] == char:
                return True
        return False
    
    def checkRightCell(self, char, row, col):
        if col + 1 < self.width:
            if self.board[row][col + 1] == char:
                return True
        return False