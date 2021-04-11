# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def depth(root: TreeNode) -> int:
            if root==None:
                return 0
            else:
                return 1+max(depth(root.left),depth(root.right))
        height=depth(root)
        def MaxSum(root:TreeNode,depth:int) -> int:
            if root==None:
                return 0
            elif depth == height:
                return root.val
            else:
                return MaxSum(root.left,depth+1)+MaxSum(root.right,depth+1)
        return MaxSum(root,1)
    
    def deepestLeavesSumV2(self, root: TreeNode) -> int:
        self.maxHeight=0
        self.maxSum=0
        def depth(root: TreeNode,d:int) -> None:
            if root==None:
                return
            else:
                if self.maxHeight<d:
                    self.maxHeight=d
                    self.maxSum=0
                if self.maxHeight==d:
                    self.maxSum+=root.val
                depth(root.left,d+1)
                depth(root.right,d+1)
        depth(root,1)
        return self.maxSum
    
    def deepestLeavesSumV3(self, root: TreeNode) -> int:
        frontier=[root]
        s=0
        while frontier:
            s=0
            newfrontier=[]
            for item in frontier:
                s+=item.val
                if item.left!=None:
                    newfrontier.append(item.left)
                if item.right!=None:
                    newfrontier.append(item.right)
            frontier=newfrontier
        return s
