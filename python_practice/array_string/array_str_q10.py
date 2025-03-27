'''
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that 
the absolute difference between any two elements of this subarray is less than or equal to limit.
'''

from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """

        """
        - keep track of max and min of the subarray
        - if max(max - min) of current subarray <= limit, then the abs diff of any two elements in
          the same subarray must be <= limit
        - two pointers to keep track of the current subarray 

        --> sliding window problem:

        - increment right normally (using a for loop)
        - get the min, max of current subarray, then check against the limit
        - if abs(diff(max, mid)) <= limit, only increment right
        - else, increment both
        - at the end of each iteration, get the size of the valid subarray, and store running longest

        """
        # longest = 0
        # for left in range(len(nums)):
        #     for right in range(left, len(nums)):
        #         max_val, min_val = max(nums[left:right + 1]), min(nums[left:right + 1])
        #         if abs(max_val - min_val) <= limit:
        #             longest = max(longest, right - left + 1)
        # return longest

        # O(N^2)


        left = 0
        longest = 0
        min_deque = deque([])
        max_deque = deque([])

        for right in range(len(nums)):
            curr = nums[right]

            while min_deque and min_deque[-1] > curr:
                min_deque.pop()
            min_deque.append(curr)

            while max_deque and max_deque[-1] < curr:
                max_deque.pop()
            max_deque.append(curr)
            
            while abs(max_deque[0] - min_deque[0]) > limit:
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                if nums[left] == min_deque[0]:
                    min_deque.popleft()
                left += 1

            longest = max(longest, right - left + 1)
        return longest
