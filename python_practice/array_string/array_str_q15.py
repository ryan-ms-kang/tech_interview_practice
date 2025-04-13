'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.
'''

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        stack = []
        curr_str, multiplier = "", ""

        while i < len(s): 
            if s[i].isnumeric():
                while i < len(s) and s[i].isnumeric():
                    multiplier += s[i]
                    i += 1     
            elif s[i] == '[':
                stack.append([curr_str, int(multiplier)])
                curr_str = ""
                multiplier = ""
                i += 1
            elif s[i].isalpha():
                while i < len(s) and s[i].isalpha():
                    curr_str += s[i]
                    i += 1
            elif s[i] == "]":
                prev_str, n = stack.pop()
                curr_str = prev_str + curr_str * n
                i += 1
        return curr_str
    
    # Time: O(N), n is len(s)