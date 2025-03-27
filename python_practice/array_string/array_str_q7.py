'''
Given a string s, find the length of the longest substring without duplicate characters.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # longest = 0
        # for slow in range(len(s)):
        #     seen = {}
        #     curr_longest = 0
        #     for fast in range(slow, len(s)):
        #         if s[fast] not in seen:
        #             seen[s[fast]] = True
        #             curr_longest += 1
        #         else:
        #             break
        #     longest = max(longest, curr_longest)
        # return longest
    
    # O(N^2)

        left = 0
        seen = {}
        longest = 0

        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1  

            seen[s[right]] = right 
            longest = max(longest, right - left + 1)  

        return longest
    
    # O(N)
            