# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum=float('-inf')
        def findMaxSum(curNode):
            if curNode==None:
                return 0
            else:
                leftMax=findMaxSum(curNode.left)
                rightMax=findMaxSum(curNode.right)
                nodePath=curNode.val+max(leftMax,rightMax,leftMax+rightMax,0)
                self.maxSum=max(self.maxSum,nodePath)
                return curNode.val+max(leftMax,rightMax,0)
        
        findMaxSum(root)
        return self.maxSum 
