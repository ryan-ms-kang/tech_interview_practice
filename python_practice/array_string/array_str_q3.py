'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        s_list = list(s)
        start, end = 0, len(s_list) - 1 
        while start < end:
            while start < end and s_list[start] not in vowels: 
                start += 1
            while start < end and s_list[end] not in vowels:  
                end -= 1 
            swap = s_list[start]
            s_list[start] = s_list[end] 
            s_list[end] = swap
            start += 1
            end -= 1
        return "".join(s_list) 
    
# Time complexity: O(N)