class TreeNode:
    def __init__(self, val=0, left=None, right=None, tag=False):
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
            # elif curNode.tag:
            #     nodePath=curNode.val+max(leftMax,rightMax,leftMax+rightMax)
            #     curNode.val+max(leftMax,rightMax,leftMax+rightMax)
            #     return curNode.val
            else:
                leftMax=findMaxSum(curNode.left)
                rightMax=findMaxSum(curNode.right)
                nodePath=0
                if curNode.tag:
                    nodePath=curNode.val+max(leftMax,rightMax)
                else:
                    nodePath=curNode.val+leftMax+rightMax
                self.maxSum=max(self.maxSum,nodePath)
                if curNode.tag:
                    return curNode.val
                else:
                    return curNode.val+max(leftMax,rightMax)
        
        findMaxSum(root)
        return self.maxSum 
left=TreeNode(2, TreeNode(25))
right=TreeNode(0, TreeNode(14,None,None,True),TreeNode(15,None,None,True))
test1=TreeNode(5,left,right)
s=Solution()
print(s.maxPathSum(test1)) #expect 47
print(s.maxPathSum(TreeNode(5, TreeNode(2, TreeNode(100, None, None, True), TreeNode(50, None, None, True), True), TreeNode(0, TreeNode(4, None, None, True), TreeNode(15, None, None, True))))) # expact 102
