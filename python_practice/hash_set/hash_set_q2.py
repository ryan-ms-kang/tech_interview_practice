'''
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
'''

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occurences = {}
        for num in arr:
            if num not in occurences:
                occurences[num] = 0
            occurences[num] += 1
        
        count = {}
        for num in occurences:
            if occurences[num] not in count:
                count[occurences[num]] = True
            else:
                return False
        return True    
    
    # Time complexity: O(N)

    '''
    Simplified; slightly optimized

    occurrences = Counter(arr)  
    return len(set(occurrences.values())) == len(occurrences.values()) 

    # Time complexity: O(N) 
    '''