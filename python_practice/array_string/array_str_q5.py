'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.
'''
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first, second = float("inf"), float("inf")
        for num in nums:
            if num < first:
                first = num
            elif first < num < second:
                second = num
            elif num > second:
                return True
        return False

# Time complexity: O(N) -> iterate through the array of length N once