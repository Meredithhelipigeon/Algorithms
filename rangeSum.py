# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def rangeSumBST(self, root, low, high):
#         """
#         :type root: TreeNode
#         :type low: int
#         :type high: int
#         :rtype: int
#         """
#         stack=[root]
#         ret=0
#         if root==None:
#             return ret
        
#         while len(stack)>0:
#             cur=stack.pop()
#             if low<=cur.val<=high:
#                 ret+=cur.val
#             if not cur.right==None:
#                 stack.append(cur.right)
#             if not cur.left==None:
#                 stack.append(cur.left)
        
#         return ret


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# make a good use of BST
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        def visit(cur):
            ret=0
            if cur==None:
                return 0
            else:
                if low<=cur.val<=high:
                    ret+=cur.val
                    ret+=(visit(cur.left)+visit(cur.right))
                elif cur.val < low:
                    ret+=visit(cur.right)
                else:
                    ret+=visit(cur.left)
            return ret
        
        return visit(root)
