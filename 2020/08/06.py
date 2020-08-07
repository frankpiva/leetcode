"""

Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

# close, no cigar
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for index, value in enumerate(nums):
            if value == False:
                continue
            else:
                nextIndex = value - 1
                lastIndex = index 
                while nums[nextIndex]:
                    nums[lastIndex] = False
                    lastIndex = nextIndex
                    nextIndex = nums[nextIndex] - 1


# closer, breaks on certain cases
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return []

        if len(nums) == 2:
            if nums[0] == nums[1]:
                return [nums[0]]
            else:
                return []

        for num in nums:
            nextIndex = nums[num] - 1
            lastIndex = num
            while nums[nextIndex]:
                nums[lastIndex] = False
                lastIndex = nextIndex
                nextIndex = nums[nextIndex] - 1
                if nextIndex < 0:
                    break

        return list(filter(lambda e: e != False, nums))


# approach: circular indexing
# memory: O(n/2)
# runtime: O(n)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicates.append(index + 1)
            nums[index] = -nums[index]
        return duplicates
