# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Step 1. a function to search path for p and q
        def findPath(curNode,v):
            if curNode==None:
                return []
            if curNode.val==v:
                return [curNode]
            else:
                left=findPath(curNode.left,v)
                right=findPath(curNode.right,v)
                if left:
                    return [curNode]+left
                if right:
                    return [curNode]+right
                return []
            
        pPath=findPath(root,p.val)
        qPath=findPath(root,q.val)
    
        # Step 2. compare two paths and find the lowest different one
        index=0
        while index<len(pPath) and index<len(qPath):
            if not pPath[index].val == qPath[index].val:
                break
            index+=1
        
        return pPath[index-1]
    
