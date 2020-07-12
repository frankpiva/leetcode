"""
Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

# approach: iterate, expand power set, add expanded set to power set at end of loop
# memory: O(2^n)
# runtime: O(2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = [[]]
        for num in nums:
            nextExpansion = []
            for subset in powerset:
                nextExpansion.append(subset + [num])
            powerset += nextExpansion
        return powerset


# approach: big brain refinement
# memory: O(2^n)
# runtime: O(2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = [[]]
        for num in nums:
            powerset += [subset + [num] for subset in powerset]
        return powerset
