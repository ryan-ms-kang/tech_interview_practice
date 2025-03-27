'''
You are given a 2D array visits, where each element represents a user visit pattern to websites. Each visit is a list of two elements:

The first element is the user’s name (a string).
The second element is a website (a string) the user visited.
The task is to return all the website patterns that are visited by at least three users. 
A pattern is a sequence of three websites that are visited in order by a user. 

For example, if a user visits websites in this order: ["a", "b", "c"], then the pattern is ("a", "b", "c").

Return the list of all distinct patterns (sorted lexicographically) that are visited by at least three users.
'''
class Solution(object):
    def distinctPatterns(self, visits):
        patterns = {}
        
        for visit in visits:
            name, websites = visit[0], visit[1:]  
            for i in range(len(websites) - 2):
                pattern = tuple(websites[i:i+3])
                if pattern not in patterns:
                    patterns[pattern] = set()
                patterns[pattern].add(name)
        
        final = []
        for pattern, users in patterns.items():
            if len(users) >= 3:  
                final.append(list(pattern))
        
        return final
