"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        def findPath(node):
            ret=[node]
            while node.parent:
                ret.append(node.parent)
                node=node.parent
            return ret
        pPath=findPath(p)
        qPath=findPath(q)
        
        i=0
        while i < min(len(pPath),len(qPath)):
            if not pPath[len(pPath)-1-i].val==qPath[len(qPath)-1-i].val:
                break
            i+=1

        return pPath[len(pPath)-i]
