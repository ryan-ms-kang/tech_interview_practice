'''
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities 
(this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.
'''

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = {}
        for road in connections:
            a, b = road[0], road[1]
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        stack = [0]
        reverse_roads = 0
        visited = set([0])
        
        while stack:
            a = stack.pop()
            for b, direction in graph.get(a):
                if b not in visited:
                    visited.add(b)
                    if direction == 1 and b != 0:
                        reverse_roads += 1
                    stack.append(b)
        return reverse_roads
            

# O(N), where N = num of cities. Each city is vsited exactly once. O(N) space from creating graph structure to store N