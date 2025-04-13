'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # longest_rep_char_length = 0
        # for left in range(len(s)):
        #     curr_rep_char_length = 0
        #     char_count = {}
        #     curr_max_freq = 0

        #     for right in range(left, len(s)):
        #         if s[right] not in char_count:
        #             char_count[s[right]] = 0
        #         char_count[s[right]] += 1

        #         curr_max_freq = max(curr_max_freq, char_count[s[right]])
        #         if (right - left + 1) - curr_max_freq <= k:
        #             curr_rep_char_length = right - left + 1
        #         else:
        #             break
                

        #     longest_rep_char_length = max(longest_rep_char_length, curr_rep_char_length)    
        # return longest_rep_char_length
    
    # Time: O(N^2), Space: O(N)

        char_count = {}
        longest = 0
        left = 0
        max_freq = 0

        for right in range(len(s)):
            if s[right] not in char_count:
                char_count[s[right]] = 0 
            char_count[s[right]] += 1

            max_freq = max(max_freq, char_count[s[right]])

            while right - left + 1 - max_freq > k:
                char_count[s[left]] -= 1
                left += 1

            longest = max(right - left + 1, longest)
            
        return longest
    
    # O(N)