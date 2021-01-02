"""
Check Array Formation Through Concatenation

You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.

 

Example 1:

Input: arr = [85], pieces = [[85]]
Output: true

Example 2:

Input: arr = [15,88], pieces = [[88],[15]]
Output: true
Explanation: Concatenate [15] then [88]

Example 3:

Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].

Example 4:

Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
Output: true
Explanation: Concatenate [91] then [4,64] then [78]

Example 5:

Input: arr = [1,3,5,7], pieces = [[2,4,6,8]]
Output: false

 

Constraints:

    1 <= pieces.length <= arr.length <= 100
    sum(pieces[i].length) == arr.length
    1 <= pieces[i].length <= arr.length
    1 <= arr[i], pieces[i][j] <= 100
    The integers in arr are distinct.
    The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).
"""

# approach: assemble the puzzle
# memory: O(n)
# runtime: O(n^2)
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # check every piece
        for piece in pieces:
            try:
                # print(f"[DEBUG] piece: {piece}")
                positions = []
                # check integers can contiguously be placed in arr
                for integer in piece:
                    # print(f"[DEBUG] integer: {integer}")
                    position = arr.index(integer)
                    # print(f"[DEBUG] position: {position}")
                    if len(positions) == 0:
                        positions.append(position)
                    elif position != positions[-1] + 1:
                        return False
                    else:
                        positions.append(position)
                    # print(f"[DEBUG] positions: {positions}, position: {position}")
            except:
                return False
        # if every piece was placed successfully, we have a match
        return True


# approach: assemble the puzzle (revised)
# memory: O(1)
# runtime: O(n^2)
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # check every piece
        for piece in pieces:
            last_position = -1
            # check integers can contiguously be placed in arr
            for integer in piece:
                # attempt to calculate the position of the integer
                try:
                    position = arr.index(integer)
                # if integer is not in arr, solution is not possible
                except:
                    return False
                # if this is the first position, add it
                if last_position == -1:
                    last_position = position
                # if this position is not +1 of previous position, solution is not possible
                elif position != last_position + 1:
                    return False
                # otherwise update the last position
                else:
                    last_position = position
        # if every piece was placed successfully, we have a match
        return True
