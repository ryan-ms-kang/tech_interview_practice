'''
An element x of an integer array arr of length m is dominant if more than half the elements of arr have a value of x.

You are given a 0-indexed integer array nums of length n with one dominant element.

You can split nums at an index i into two arrays nums[0, ..., i] and nums[i + 1, ..., n - 1], but the split is only valid if:

0 <= i < n - 1
nums[0, ..., i], and nums[i + 1, ..., n - 1] have the same dominant element.
Here, nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j, 
both ends being inclusive. Particularly, if j < i then nums[i, ..., j] denotes an empty subarray.

Return the minimum index of a valid split. If no valid split exists, return -1.
'''
from collections import Counter

class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_freq = {}
        right_freq = Counter(nums)

        for i in range(len(nums)):
            left_freq[nums[i]] = left_freq.get(nums[i], 0) + 1
            right_freq[nums[i]] -= 1

            if self.dominant(left_freq, i + 1) == self.dominant(right_freq, len(nums) - i - 1):
                return i
        return -1
    
    def dominant(self, freq, arr_length):
        for num, count in freq.items():
            if count > arr_length // 2:
                return num
        return None

    # Time: O(N^2)

