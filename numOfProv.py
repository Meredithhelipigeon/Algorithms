class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def explore(i):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]==1 and visited[j]==False:
                    visited[j]=True
                    explore(j)
        
        visited=[False]*len(isConnected)
        ret=0
        
        for i in range(len(isConnected)):
            if visited[i]==False:
                visited[i]=False
                explore(i)
                ret+=1
        return ret
