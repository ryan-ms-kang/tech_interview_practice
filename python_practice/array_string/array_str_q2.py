'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        plant = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and self.can_plant(i, flowerbed):
                flowerbed[i] = 1
                plant += 1
        return plant >= n
    
    def can_plant(self, i, flowerbed):
        if (i - 1 < 0 or flowerbed[i - 1] == 0) and (i + 1 >= len(flowerbed) or flowerbed[i + 1] == 0):
            return True
        else: 
            return False

# Time complexity: O(N) where  n == len(flowerbed)