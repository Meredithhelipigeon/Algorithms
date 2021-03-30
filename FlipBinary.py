# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        ans = []
        frontier = collections.deque()
        if root != None:
            frontier.append(root)
        else:
            return [-1]
        i = 0
        while len(frontier) > 0:
            item = frontier.popleft()
            if len(voyage) <= 0 or item.val != voyage[i]:
                return [-1]
            if item.left != None and item.left.val != voyage[i+1]:
                ans.append(item.val)
                frontier.appendleft(item.left)
                if item.right != None:
                    frontier.appendleft(item.right)
            else:
                if item.right != None:
                    frontier.appendleft(item.right)
                if item.left != None:
                    frontier.appendleft(item.left)
            i += 1
        
        return ans    
                
