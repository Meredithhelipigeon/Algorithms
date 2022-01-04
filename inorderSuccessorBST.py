# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        if root==None or p==None:
            return None
        successor = None
        successorVal = float('inf')
        
        #  binary search to locate the point
        #  O(logn-logm)    
        cur = root
        while cur.val != p.val:
            if cur.val > p.val:
                if successorVal > cur.val:
                    successorVal = cur.val
                    successor = cur
                cur = cur.left
            else:
                cur = cur.right
        
        # find the leftmost node in the right child p
        #  O(logm)       
        leftmostRight = p.right
        if leftmostRight==None:
            return successor
        while leftmostRight.left:
            leftmostRight = leftmostRight.left
        if successorVal > leftmostRight.val:
            successorVal = leftmostRight.val
            successor = leftmostRight
        
        return successor
