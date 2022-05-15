# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: find the deepest layer and also always update the deepest layer sum
# Time: O(n); Space: O(1)
# DFS
class Solution1(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret_pair=[0,0]
        
        def find_deepest(cur,height):
            if cur==None:
                return
            if height==ret_pair[0]:
                ret_pair[1]+=cur.val
            elif height>ret_pair[0]:
                ret_pair[0]=height
                ret_pair[1]=cur.val
            find_deepest(cur.left,height+1)
            find_deepest(cur.right,height+1)
        
        find_deepest(root,0)
        return ret_pair[1]

# Solution 2:
