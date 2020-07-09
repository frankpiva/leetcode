"""
3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

# approach: small brain iterate and calculate
# memory: > O(n^2)
# runtime: > O(n^3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # short circuit case: nums == []
        if nums == []: return 

        # create and populate a dictionary of numbers
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        # create and populate a list of solutions
        solutions = []
        for n1 in d:
            for n2 in d:
                dif = 0 - n1 - n2
                # print('dif', dif)
                if n1 in d and n2 in d and dif in d:
                    tmp = [n1, n2, dif]
                    tmp.sort()
                    # all #s are unique
                    if n1 != n2 and n2 != dif and dif != n1:
                        solutions.append(tmp)
                    else: # we have duplicates
                        # print('duplicates', tmp)
                        if n1 == n2 == dif:
                            if d[n1] > 2:
                                solutions.append(tmp)
                        elif n1 == n2 or n1 == dif:
                            if d[n1] > 1:
                                solutions.append(tmp)
                        else:
                            if d[n2] > 1:
                                solutions.append(tmp)

        # remove duplicates
        for index, solution in enumerate(solutions):
            try:
                while solutions.index(solution, index+1):
                    solutions.pop(solutions.index(solution, index+1))
            except:
                pass

        return solutions

# approach: sort, loop, and squeeze
# memory: O(n^2ish) ? [-1,0,1] = 1 solution, [-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8] = 32 solutions
# runtime: O(nlog(n)*n*log(n)) =? O(2*n^2*log(n))
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # short circuit case: nums == []
        if nums == []: return 

        # sort the input list, create and populate a list of solutions
        nums.sort()
        solutions = []
        for i in range(len(nums)-2):
            # if we're the first element or not a duplicate
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                low = i + 1
                high = len(nums) - 1
                dif = 0 - nums[i]

                while low < high:
                    # we found a perfect match
                    if nums[low] + nums[high] == dif:
                        solutions.append([nums[i], nums[low], nums[high]])
                        # skip over duplicates
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < dif:
                        low += 1
                    else:
                        high -= 1

        return solutions
