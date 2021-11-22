# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
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
root=TreeNode(5, TreeNode(2, TreeNode(100), TreeNode(50)), TreeNode(0, TreeNode(4), TreeNode(15)))
s=Solution()
print(s.maxPathSum(root)) # expact 152
