# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret=[]
        def visit(node,level):
            if node:
                if len(ret)>level:
                    ret[level]=node.val
                else:
                    ret.append(node.val)
                if node.left:
                    visit(node.left,level+1)
                if node.right:
                    visit(node.right,level+1)
        visit(root,0)
        return ret
