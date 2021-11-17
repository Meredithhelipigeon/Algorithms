import queue
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        distances = [[0]*len(grid[0]) for i in range(len(grid))]
        numBuildings=[[0]*len(grid[0]) for i in range(len(grid))]
        self.directions = [[0,1],[0,-1],[1,0],[-1,0]]
        def bfs(pos,k):
            q=deque()
            q.append([pos,0])
            while q:
                curPos,dis=q.popleft()
                for d in self.directions:
                    if 0<=curPos[0]+d[0]<len(grid) and 0<=curPos[1]+d[1]<len(grid[0]) and grid[curPos[0]+d[0]][curPos[1]+d[1]]==0 and numBuildings[curPos[0]+d[0]][curPos[1]+d[1]]==k:
                        numBuildings[curPos[0]+d[0]][curPos[1]+d[1]]+=1
                        distances[curPos[0]+d[0]][curPos[1]+d[1]]+=dis+1
                        q.append([[curPos[0]+d[0],curPos[1]+d[1]],dis+1])
                        
        k=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    bfs([i,j],k)
                    k+=1
                    
        ret=float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if numBuildings[i][j]==k:
                    ret=min(distances[i][j],ret)
        return ret if ret!=float('inf') else -1

