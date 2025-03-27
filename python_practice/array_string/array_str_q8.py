'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        prev = intervals[0]

        for curr in intervals[1:]:
            if prev[1] >= curr[0]:
                merged = [prev[0], max(prev[1], curr[1])]
                prev = merged
            else:
                result.append(prev)
                prev = curr

        result.append(prev)
        return result
                

# Time is O(N log N), Space is O(N)