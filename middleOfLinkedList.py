# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lastOne = head
        lastTwo = head
        while lastTwo and lastTwo.next:
            lastOne = lastOne.next
            lastTwo = lastTwo.next.next
        
        return lastOne
