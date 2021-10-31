class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited=[[False]*len(grid[0]) for i in range(len(grid))]
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        
        def explore(cur,index):
            i,j=cur[0],cur[1]
            grid[i][j]=index
            ret=1
            for d in direction:
                if 0<=i+d[0]<len(grid) and 0<=j+d[1]<len(grid[0]) and grid[i+d[0]][j+d[1]]==1:
                    ret+=explore([i+d[0],j+d[1]],index)
            return ret
        
        index=2
        spaceArray=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    space=explore([i,j],index)
                    spaceArray.append(space)
                    index+=1
        if len(spaceArray)==0:
            return 1
        maxIsland=max(spaceArray)  
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    total=1
                    islandSet=set()
                    for d in direction:
                        if 0<=i+d[0]<len(grid) and 0<=j+d[1]<len(grid[0]) and grid[i+d[0]][j+d[1]]>0 and not grid[i+d[0]][j+d[1]] in islandSet:
                            total+=spaceArray[grid[i+d[0]][j+d[1]]-2]
                            islandSet.add(grid[i+d[0]][j+d[1]])
                    if total>maxIsland:
                        maxIsland=total
        
        return maxIsland
        
