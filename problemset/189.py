"""
189. Rotate Array
Medium

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

 

Constraints:

    1 <= nums.length <= 2 * 104
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105
"""

# approach: dynamic programming
# memory: O(n)
# runtime: O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # identify rotational axis
        if k > len(nums):
            k = k % len(nums)
        
        # create a deep copy to store lookup values
        tmp = copy.deepcopy(nums)
        
        # populate lookup values
        for i in range(len(nums)):
            if i < k:
                tmp[i] = nums[len(nums) - k + i]
            else:
                tmp[i] = nums[i - k]

        # assign lookup values
        for i in range(len(nums)):
            nums[i] = tmp[i]
