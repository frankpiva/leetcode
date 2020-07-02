"""
1. Two Sum
Easy

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

# approach: brute force with short circuit cases
# memory: O(1)
# runtime: O(n^n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
            
        for num in nums:
            difference = target - num
            if num == difference:
                if nums.count(difference) > 1:
                    a = nums.index(num)
                    b = nums.index(difference, a+1)
                    return [a, b]
            elif nums.count(difference) > 0:
                a = nums.index(num)
                b = nums.index(difference)
                return [a, b]