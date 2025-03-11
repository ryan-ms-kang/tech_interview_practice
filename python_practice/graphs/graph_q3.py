'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, 
and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, 
and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
'''

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        total_num_provinces = 0
        seen = set()

        for city in range(len(isConnected)):
            if city not in seen:
                stack = [city]
                while stack:
                    i = stack.pop()
                    for j in range(len(isConnected[i])):
                        if j not in seen and isConnected[i][j] == 1:
                            seen.add(j)
                            stack.append(j)
                total_num_provinces += 1
        return total_num_provinces
        
            