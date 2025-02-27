'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
'''

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        i_to_modify = 0

        while i < len(chars):
            curr_char = chars[i]
            curr_char_count = 0

            while i < len(chars) and chars[i] == curr_char:
                curr_char_count += 1
                i += 1

            chars[i_to_modify] = curr_char
            i_to_modify += 1

            if curr_char_count > 1:
                for num in str(curr_char_count):
                    chars[i_to_modify] = num
                    i_to_modify += 1
            
        return i_to_modify
    
