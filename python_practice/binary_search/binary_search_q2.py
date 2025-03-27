'''
You are given two positive integer arrays spells and potions, of length n and m respectively, 
where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.
'''

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """

        # Optimized time: O(Nlog M); N * O(log M) for each spell, where N = num of spells and M = num of potions.
        # Binary search takes O(log M), sorting takes M log M for M potions

        potions = sorted(potions)
        pairs = []

        for spell in spells:
            start, end = 0, len(potions) - 1

            while start <= end:
                mid = (end + start) // 2
                curr_prod = potions[mid] * spell
                
                if curr_prod >= success:
                    end = mid - 1
                else:
                    start = mid + 1

            pairs.append(len(potions) - start)
        return pairs


        # # Time: O(N x M), where N = nbum of spells and M = num of potions. Space: O(N)

        # pairs = []
        # for spell in spells:
        #     num_success = 0
        #     for potion in potions:
        #         if spell * potion >= success:
        #             num_success += 1
        #     pairs.append(num_success)
        # return pairs
    