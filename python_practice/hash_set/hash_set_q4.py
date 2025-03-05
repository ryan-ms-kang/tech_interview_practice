'''
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
'''

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        '''
        one, two = Counter(word1), Counter(word2)
        return set(one.keys()) == set(two.keys()) and sorted(one.values()) == sorted(two.values())

        # O((N + M)log(N + M)), where N is # of elements in word1 and M is for word2
        '''

        one, two = Counter(word1), Counter(word2)
        one_count_freq = Counter(one.values())
        for count in two.values():
            if count in one_count_freq:
                one_count_freq[count] -= 1
            else:
                return False
            if one_count_freq[count] < 0:
                return False
        
        for count_freq in one_count_freq.values():
            if count_freq != 0:
                return False
        return set(one.keys()) == set(two.keys())
    
        # O(N + M + K), where N = len(word1), M = len(word2), and k = # of distinct frequencies in word1
