# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        def depth(v):
            l=[[root,0]]
            if root.val==v:
                return (None,0)
            while len(l)>0:
                cur,i=l.pop()
                if cur==None:
                    continue
                if not cur.left==None:
                    if cur.left.val==v:
                        return (cur,i+1)
                    l.append([cur.left,i+1])
                if not cur.right==None:
                    if cur.right.val==v:
                        return (cur,i+1)
                    l.append([cur.right,i+1])
            return -1

        pX,dX=depth(x)
        pY,dY=depth(y)
        if dX==dY and (not pX==pY):
            return True
        else:
            return False
