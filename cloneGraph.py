"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node==None:
            return None
        visited=[False]*100
        start=node
        q=deque()
        
        cur=Node(start.val,start.neighbors)
        visited[cur.val-1]=cur
        q.append(cur)
        
        while len(q)>0:
            cc=q.popleft()
            curNeg=cc.neighbors
            cc.neighbors=[]
            for nn in curNeg:
                if visited[nn.val-1]==False:
                    copy=Node(nn.val,nn.neighbors)
                    cc.neighbors.append(copy)
                    visited[copy.val-1]=copy
                    q.append(copy)
                else:
                    cc.neighbors.append(visited[nn.val-1])
        
        return cur
