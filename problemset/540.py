"""
540. Single Element in a Sorted Array
Medium

3934

98

Add to List

Share
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        # start at both ends and find the midpoint
        while left < right:
            mid = right - (right - left) // 2
            # if the remainder in each side is even, offset needs to be the same
            if mid % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    right = mid - 2
                else:
                    left = mid
            # else the remainder in each side is odd, offset needs to be different
            else:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    right = mid - 1

        # adjust for overshoot
        if left == right:
            return nums[left]
        else:
            return nums[mid + 1]
