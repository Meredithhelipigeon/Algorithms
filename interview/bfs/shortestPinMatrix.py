import queue
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0]==1:
            return -1
        q = queue.Queue()
        q.put([1,(0,0)])
        dest=(len(grid)-1,len(grid)-1)
        neighbours=[(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        grid[0][0]=1
        
        while q.qsize()>0:
            curDis,curPos=q.get()
            if curPos==dest:
                return curDis
            for n in neighbours:
                h,v=n
                if 0<=curPos[0]+h<len(grid) and 0<=curPos[1]+v<len(grid) and grid[curPos[0]+h][curPos[1]+v]==0:
                    grid[curPos[0]+h][curPos[1]+v]=1
                    q.put([curDis+1,(curPos[0]+h,curPos[1]+v)])    
        
        return -1
