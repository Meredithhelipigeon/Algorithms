# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        ret=[]
        cur=head
        while cur!=None:
            ret.append(cur.val)
            cur=cur.next
        ret=sorted(ret)
        cur2=head
        index=0
        while cur2!=None:
            cur2.val=ret[index]
            index+=1
            cur2=cur2.next
        return head
