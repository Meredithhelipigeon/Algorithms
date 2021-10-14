# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        nodeList=[]
        curNode=TreeNode(preorder[0])
        root=curNode
        
        for i in range(1,len(preorder)):
            n=TreeNode(preorder[i])
            if curNode.val > preorder[i]:
                curNode.left=n
                nodeList.append(curNode)
                curNode=n
            else:
                if len(nodeList)==0:
                    curNode.right=n
                    curNode=n
                else:
                    parent=nodeList.pop()
                    while preorder[i]>parent.val:
                        curNode=parent
                        if not len(nodeList)==0:
                            parent=nodeList.pop()
                        else:
                            parent=None
                            break
                    if not parent == None:
                        nodeList.append(parent)
                    curNode.right=n
                    curNode=n
        
        return root
