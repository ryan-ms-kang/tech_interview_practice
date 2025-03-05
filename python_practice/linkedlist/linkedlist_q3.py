'''
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, 
where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Single loop

        if not head or not head.next:
            return None

        prev = slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head

        '''
        # Two loops

        if not head or not head.next:
            return None
            
        size = 0
        dummy = head
        while dummy:
            dummy = dummy.next
            size += 1
        
        prev = None
        dummy = head
        for i in range(size // 2):
            prev = dummy
            dummy = dummy.next
        prev.next = dummy.next 
        return head
        '''