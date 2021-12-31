# Given the root of a binary tree, find the maximum value v for which 
# there exist different nodes a and b where v = |a.val - b.val| and a 
# is an ancestor of b.

# A node a is an ancestor of b if either: any child of a is equal to b
#  or any child of a is an ancestor of b.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution: The maximum difference for a node is (node.val, min(node.desc), max(node.desc)) => pass elements up.
# Or we can calculate by (node.val, min(node.acsc), max(node.acsc)) => pass elements down.

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0
        def find_max_min_pair(n):
            if n==None:
                return [float('inf'),float('-inf')]
            leftPair = find_max_min_pair(n.left)
            rightPair = find_max_min_pair(n.right)
            curMin = min(leftPair[0],rightPair[0]) 
            curMax = max(leftPair[1],rightPair[1])
            curMin = n.val if curMin ==float('inf') else curMin
            curMax = n.val if curMax ==float('-inf') else curMax
            self.ret = max(abs(n.val-curMin),abs(n.val-curMax),self.ret)
            return [min(n.val,curMin),max(n.val,curMax)]
        
        find_max_min_pair(root)
        return self.ret
    
    def maxAncestorDiff2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0
        
        def update_max_diff(n,cur_max,cur_min):
            if n==None:
                return
            self.ret=max(self.ret,abs(n.val-cur_max),abs(n.val-cur_min))
            update_max_diff(n.left,max(cur_max,n.val),min(cur_min,n.val))
            update_max_diff(n.right,max(cur_max,n.val),min(cur_min,n.val))
        
        update_max_diff(root,root.val,root.val)
        return self.ret
