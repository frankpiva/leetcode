"""
6. ZigZag Conversion
Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

# approach: naive iterative solution
# memory: O(~n^2)
# runtime: O(~n^2) 
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # build a matrix to store the pattern
        matrix = []
        for i in range(0, numRows): matrix.append([])

        # populate the matrix
        index = 0
        while index < len(s):
            row = 0
            # insert values vertically, descending
            for i in range(0, numRows):
                matrix[row].append(s[index])
                index += 1
                row += 1
                if index >= len(s): break
            # insert values for spacer columns
            for j in range(0, numRows - 2):
                # reset row to bottom of column
                row = len(matrix) - 1
                # insert values vetically, ascending
                for k in range(0, numRows):
                    # if k is diagonal, insert value, else insert space
                    if k == j+1:
                        if index < len(s):
                            matrix[row].append(s[index])
                            index += 1
                            if index >= len(s): break
                    else:
                        matrix[row].append(' ')
                    row -= 1

        # format and return string
        formatted = ''
        for row in matrix:
            formatted += ''.join(row)
        return formatted.replace(' ', '')
