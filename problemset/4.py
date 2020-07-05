"""
4. Median of Two Sorted Arrays
Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

# approach: median of one (combine and sort if necessary)
# memory: O(m+n)
# runtime: O(log(m+n))
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # short circuit case: [], []
        if nums1 == [] and nums2 == []:
            return []
        
        # short circuit case: [], [...]
        if nums1 == []:
            return self.medianOfOne(nums2)
        
        # short circuit case: [...], []
        if nums2 == []:
            return self.medianOfOne(nums1)
        
        # everything else <-- gross, but I'm lazy
        everything = nums1 + nums2
        everything.sort()
        return self.medianOfOne(everything)


    def medianOfOne(self, array):
        length = len(array)
        midpoint = int(length / 2)        
        if length % 2 == 1:
            return array[midpoint]
        else:
            return (array[midpoint - 1] + array[midpoint]) / 2.0