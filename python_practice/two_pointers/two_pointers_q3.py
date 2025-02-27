'''
You are given an integer array height of length n. There are n vertical lines drawn such that 
the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_amount = -float("inf")
        while left < right:
            curr_amount = min(height[left], height[right]) * (right - left)
            max_amount = max(max_amount, curr_amount)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_amount

# Time complexity: O(N)