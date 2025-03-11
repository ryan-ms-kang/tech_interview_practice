'''
You are given an array of variable pairs equations and an array of real numbers values, 
where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. 
Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.
'''

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}
        for i in range(len(equations)):
            a, b = equations[i][0], equations[i][1]
            if a not in graph: 
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        answers = []
        for query in queries:
            start, end = query[0], query[1]

            if start not in graph or end not in graph:
                answers.append(-1.0)
                continue

            seen = set((start))
            stack = [(start, 1)]
            found = False

            while stack and not found:
                node, curr_prod = stack.pop()
                for var, val in graph[node]:
                    if var == end:
                        answers.append(curr_prod * val)
                        found = True
                        break
                    elif var not in seen:
                        stack.append((var, curr_prod * val))
                        seen.add(var)
                
            if not found:
                answers.append(-1.0)
        return answers

