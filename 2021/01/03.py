"""
Beautiful Arrangement

Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

    perm[i] is divisible by i.
    i is divisible by perm[i].

Given an integer n, return the number of the beautiful arrangements that you can construct.

 

Example 1:

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1

Example 2:

Input: n = 1
Output: 1

 

Constraints:

    1 <= n <= 15
"""

# approach: recursion with early exit
# memory: O(B), where B is the number of beautiful arrangements
# runtime: O(B), where n is the number of beautiful arrangements
class Solution:
    def countArrangement(self, n: int) -> int:
        # initialize
        self.count = 0
        self.nums = list(range(1, n + 1))
        self.permute(0)
        return self.count

    def permute(self, j: int) -> None:
        # we reached the end of a valid permutation
        if j == len(self.nums):
            self.count += 1
        # otherwise keep iterating, swapping, and recursing
        for i in range(j, len(self.nums)):
            # first iteration swaps the same element, serving as a branch for subsequent swaps
            self.swap(i, j)
            # recurse and progress if the current permutation is valid
            if (self.nums[j] % (j + 1) == 0) or ((j + 1) % self.nums[j] == 0):
                self.permute(j + 1)
            # backtrack
            self.swap(i, j)
    
    def swap(self, i: int, j: int) -> None:
        t = self.nums[i]
        self.nums[i] = self.nums[j]
        self.nums[j] = t
