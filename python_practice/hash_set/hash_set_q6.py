'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.

bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.

int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). 
Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.
'''

import random 

class RandomizedSet(object):

    def __init__(self):
        self.list_of_nums = []
        self.dict_of_nums = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.dict_of_nums:
            self.list_of_nums.append(val)
            self.dict_of_nums[val] = len(self.list_of_nums) - 1
            return True
        return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict_of_nums:
            old_val_index = self.dict_of_nums[val]
            end_val = self.list_of_nums[-1]

            self.list_of_nums[old_val_index] = end_val
            self.dict_of_nums[end_val] = old_val_index

            self.list_of_nums.pop()
            self.dict_of_nums.pop(val)

            return True
        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        
        return random.choice(self.list_of_nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()