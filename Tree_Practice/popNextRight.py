"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# Populating Next Right Pointers in Each Node

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        lastLevelFirst = root
        
        while lastLevelFirst:
            # for each level
            lastLevelCur = lastLevelFirst
            last = None
            while lastLevelCur:
                if last:
                    last.next = lastLevelCur.left
                else:
                    lastLevelFirst = lastLevelCur.left
                if lastLevelCur.left:
                    lastLevelCur.left.next = lastLevelCur.right
                last=lastLevelCur.right
                lastLevelCur = lastLevelCur.next
        return root
