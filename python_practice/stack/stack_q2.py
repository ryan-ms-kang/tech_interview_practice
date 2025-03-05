'''
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
'''

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stars_removed = []
        for char in s:
            if char == "*":
                stars_removed.pop()
            else:
                stars_removed.append(char)
        return "".join(stars_removed)
    
# O(N); N characters in s to add/pop, another N to join all the chars in stars_removed arr