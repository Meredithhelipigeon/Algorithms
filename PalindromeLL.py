# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = []
        
        while head != None :
            l.append(head.val)
            head = head.next
        
        num = len(l)/2
        i = 0
        while i<num:
            if l[i] != l[len(l)-1-i]:
                return False
            i+=1
        
        return True

    def isPalindromeV2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        i = 0
        oldCur = None
        newCur = head
        Walk = head
        while Walk != None:
            i += 1
            Walk = Walk.next
            if i%2 == 0:
                saveNew = newCur.next
                newCur.next = oldCur
                oldCur = newCur
                newCur = saveNew
        
        List1 = oldCur
        List2 = None
        if i%2 == 0:
            List2 = newCur
        elif newCur != None:
            List2 = newCur.next

        while List1 != None and List2 != None:
            if List1.val != List2.val:
                return False
            List1=List1.next
            List2=List2.next        
            
        return True
    def reverseList(self,start,end):
            cur = start
            oldcur = None
            while cur!=end:
                newcur=cur.next
                cur.next=oldcur
                oldcur=cur
                cur=newcur
            return oldcur
    def isPalindromeV3(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # fast and slow algorithm
        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            
        List1=self.reverseList(head,slow)
        List2=None
        if fast == None:
            List2=slow
        else:
            List2=slow.next
        
        while List2 != None:
            if List1.val != List2.val:
                return False
            List1=List1.next
            List2=List2.next
            
        return True
