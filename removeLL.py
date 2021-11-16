# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        last=None
        cur=head
        ret=None
        while cur:
            n=cur.next
            if cur.val==val:
                if last:
                    last.next=n
                cur=n
                continue
            elif ret==None:
                ret=cur
            last=cur
            cur=n
        
        return ret
