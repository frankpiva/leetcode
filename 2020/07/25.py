"""
Find Minimum in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1

Example 2:

Input: [2,2,2,0,1]
Output: 0

Note:

    This is a follow up problem to Find Minimum in Rotated Sorted Array.
    Would allow duplicates affect the run-time complexity? How and why?
"""

# approach: linear check with early exit
# memory = O(1)
# runtime = O(n)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # handle bad input
        if nums == []:
            return nums

        # initialize minimum, start checking
        minimum = nums[0]
        for num in nums:
            # if new minimum is discovered, we found the pivot
            if num < minimum:
                minimum = num
                break

        return minimum
