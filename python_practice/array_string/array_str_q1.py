'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        alt = True
        p1, p2 = 0, 0
        while p1 < len(word1) and p2 < len(word2):
            if alt:
                merged += word1[p1]
                p1 += 1
                alt = False
            else:
                merged += word2[p2]
                p2 += 1
                alt = True
        if p1 < len(word1):
            merged += word1[p1:]
        if p2 < len(word2):
            merged += word2[p2:]
        return merged
    
    # Time complexity: O(N + M) where N is len(word1) and M is len(word2) 
     