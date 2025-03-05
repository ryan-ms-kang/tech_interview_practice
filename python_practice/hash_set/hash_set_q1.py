'''
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
'''

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        not_in_1, not_in_2 = set(), set()
        nums_in_1, nums_in_2 = {}, {}

        for num in nums1:
            if num not in nums_in_1:
                nums_in_1[num] = 1
        for num in nums2:
            if num not in nums_in_1:
                not_in_1.add(num)

        for num in nums2:
            if num not in nums_in_2:
                nums_in_2[num] = 1
        for num in nums1:
            if num not in nums_in_2:
                not_in_2.add(num)
        
        return [list(not_in_2), list(not_in_1)]

        # Time complexity: O(2N + 2M), amortized O(N);  where N = len(num1) and M = len(nums2)

        '''
        # Slightly optimized

        distinct_1, distinct_2 = set(nums1), set(nums2)
        return [list(distinct_1 - distinct_2), list(distinct_2 - distinct_1)]

        # Time complexity: O(N + M) amortized O(N); where N = len(num1) and M = len(nums2)
        '''
