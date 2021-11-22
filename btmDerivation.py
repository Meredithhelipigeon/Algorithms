# Definition for a binary tree node.
class TreeNode:
    def __init__(self, tag, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.tag = tag
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum=float('-inf')
        def findMaxSum(curNode):
            if curNode==None:
                return float('-inf')
            else:
                leftMax=findMaxSum(curNode.left)
                rightMax=findMaxSum(curNode.right)
                nodePath=0
                if curNode.tag:
                    nodePath=curNode.val+max(leftMax,rightMax,leftMax+rightMax)
                else:
                    nodePath=curNode.val+leftMax+rightMax
                self.maxSum=max(self.maxSum,nodePath)
                retCur=curNode.val 
                if curNode.tag:
                    return curNode.val+max(leftMax,rightMax,0)
                else:
                    return curNode.val+max(leftMax,rightMax)
        
        findMaxSum(root)
        return self.maxSum 

left=TreeNode(False, 2, TreeNode(True,25))
right=TreeNode(False, 0, TreeNode(True,14),TreeNode(True,15))
test1=TreeNode(False,5,left,right)
s=Solution()
print(s.maxPathSum(test1))
