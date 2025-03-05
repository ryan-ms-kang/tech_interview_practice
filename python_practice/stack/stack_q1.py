'''
We are given an array asteroids of integers representing asteroids in a row. 
The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). 
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
'''

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        state = []
        for roid in asteroids: 
            # Collision occurs when top roid is moving right/pos AND new roid is moving left/neg
            while state and state[-1] > 0 and roid < 0:
                # Pop top roid (loop) until the top roid >= curr roid
                if abs(state[-1]) < abs(roid):
                    state.pop()
                    continue
                # Both top and curr roid have same abs size, so both get destroyed. End the loop
                elif abs(state[-1]) == abs(roid):
                    state.pop()
                    break
                # End the loop when top roid is bigger or destroy the curr roid
                else:
                    break
            else:
                state.append(roid)
        return state

# O(N) + O(N) = O(N); each roid is added or popped at most once