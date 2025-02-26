'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix_arr, suffix_arr = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            prefix_arr[i] = nums[i - 1] * prefix_arr[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suffix_arr[i] = nums[i + 1] * suffix_arr[i + 1]    
        answers = []
        for i in range(len(nums)):
            answers.append(prefix_arr[i] * suffix_arr[i])
        return answers
    
# Time complexity: O(N)