'''
You are given a string num representing a palindromic integer. You need to find the next lexicographically greater 
palindromic permutation of its digits. If no such number exists, return "-1".

Example Walkthrough
num = "1221" → Output: "2112"

num = "32123" → Output: "-1" (No larger palindrome possible)
'''

class Solution(object):
    def next_greatest_palindrome(self, nums):
        nums = list(str(nums))
        mid = len(nums) // 2
        stack = []
        answer = []

        for i, num in enumerate(nums[:mid]):
            if i == mid - 2:
                stack.append(nums[mid - 1])
                answer.append(nums[mid - 1])
            elif i == mid - 1:
                stack.append(nums[mid - 2])
                answer.append(nums[mid - 2])
            else:
                stack.append(nums[i])
                answer.append(nums[i])

        if len(nums) % 2 != 0:
            answer.append(nums[mid])
        
        while stack:
            answer.append(stack.pop())
        print(answer)
        answer = int("".join(answer))
        nums = int("".join(nums))

        return answer if int(answer) > int(nums) else -1
        
derp = Solution()
num = 2468642
print(derp.next_greatest_palindrome(num))