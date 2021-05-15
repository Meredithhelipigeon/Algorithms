# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack=[root]
        if root==None:
            return
        while len(stack) > 0:
            cur=stack.pop()
            if cur.right!=None:
                stack.append(cur.right)
            if cur.left!=None:
                stack.append(cur.left)
            if len(stack)!=0:
                cur.right=stack[-1]
            else:
                cur.right=None
            cur.left=None
