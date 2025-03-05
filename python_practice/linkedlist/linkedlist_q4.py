'''
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list 
is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        '''
        # Two iterations over the linkedlist; Time: O(N), Space: O(N) since I'm creating a dictionary to store N nodes

        n = 0
        nodes = {}
        while head:
            nodes[n] = head.val
            n += 1
            head = head.next

        max_twin_sum = -float("inf")
        for i in nodes:
            max_twin_sum = max(max_twin_sum, nodes[n - 1 - i] + nodes[i])
        return max_twin_sum
        '''

        # One iteration; Time: O(N), Space: O(1) since no new space is created to store the nodes/values

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        max_twin = -float("inf")
        second_half_rev = self.reverseList(slow)

        while second_half_rev:
            max_twin = max(max_twin, second_half_rev.val + head.val)
            head = head.next
            second_half_rev = second_half_rev.next
        return max_twin
    
    def reverseList(self, head):
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
        