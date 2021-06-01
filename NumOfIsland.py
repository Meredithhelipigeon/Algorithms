class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        gridMark=[[False for i in range(len(grid[0]))] for j in range(len(grid))]
        direction = [[0,-1],[0,1],[1,0],[-1,0]]
        width=len(grid[0])
        length=len(grid)
        ans=0
        for i in range(length):
            for j in range(width):
                if grid[i][j]=="1" and gridMark[i][j]==False:
                    ans+=1
                    cluster=[[i,j]]
                    gridMark[i][j]=True
                    while len(cluster)>0:
                        nCluster=[]
                        for e in cluster:
                            for d in direction:
                                if 0<=e[0]+d[0]<length and 0<=e[1]+d[1]<width and grid[e[0]+d[0]][e[1]+d[1]]=="1" and gridMark[e[0]+d[0]][e[1]+d[1]]==False:
                                    gridMark[e[0]+d[0]][e[1]+d[1]]=True
                                    nCluster.append([e[0]+d[0],e[1]+d[1]])
                        cluster=nCluster
                    
        return ans
