'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagrams = {}
        for word in strs:
            frequency = [0] * 26
            for char in word:
                frequency[ord(char) - ord('a')] += 1
            frequency = tuple(frequency)
            if frequency not in anagrams:
                anagrams[frequency] = []
            anagrams[frequency].append(word)
        return anagrams.values()
    
        # O(N * M) where N = number of words in strs and M is avergae length of each word

        # anagrams = {}
        # for word in strs:
        #     word_sorted = "".join(sorted(word))
        #     if word_sorted not in anagrams:
        #         anagrams[word_sorted] = []
        #     anagrams[word_sorted].append(word)
        # return anagrams.values()
            
    # Time: O(M * NlogN) where M is number of words in strs and N is length of each word 
