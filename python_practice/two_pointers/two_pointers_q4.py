'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
'''
import collections
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        """
        # Brute Force: O(N^2)
        
        operations = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == k:
                    nums[i] = float("inf")
                    nums[j] = float("inf")
                    operations += 1
        return operations
        """

        """
        # Time complexity: O(NlogN) from sorted()

        nums = sorted(nums)
        operations = 0
        left, right = 0, len(nums) - 1
        
        while left < right:
            if nums[left] + nums[right] == k:
                nums[left] = float("inf")
                nums[right] = float("inf")
                left += 1
                right -= 1
                operations += 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return operations
        """

        max_operations = 0
        frequency = collections.Counter(nums)

        for num in nums:
            diff = k - num
            if diff in frequency:
                if diff == num and frequency[diff] >= 2:
                    frequency[diff] -= 2
                    max_operations += 1
                elif diff != num and frequency[diff] > 0 and frequency[num] > 0:
                    frequency[num] -= 1
                    frequency[diff] -= 1
                    max_operations += 1
        return max_operations
    
        # O(N)