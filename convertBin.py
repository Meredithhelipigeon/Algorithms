"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        nodeList=[]
        if root==None:
            return None
        def calculate(cur):
            if cur==None:
                return
            left=calculate(cur.left)
            nodeList.append(cur)
            right=calculate(cur.right)
            return cur
        
        calculate(root)
        
        for i in range(0,len(nodeList)-1):
            nodeList[i].right=nodeList[i+1]
            nodeList[i+1].left=nodeList[i]
        
        nodeList[-1].right=nodeList[0]
        nodeList[0].left=nodeList[-1]
        
        return nodeList[0]
