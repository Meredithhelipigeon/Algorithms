class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m,n=len(rooms),len(rooms[0])
        dirs=[[-1,0],[1,0],[0,-1],[0,1]]
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    visited=[[False]*n for p in range(m)]
                    q=deque()
                    q.append([(i,j),0])
                    while len(q)>0:
                        cur,steps=q.popleft()
                        for d in dirs:
                            if 0<=cur[0]+d[0]<m and 0<=cur[1]+d[1]<n and rooms[cur[0]+d[0]][cur[1]+d[1]]>0 and visited[cur[0]+d[0]][cur[1]+d[1]]==False:
                                visited[cur[0]+d[0]][cur[1]+d[1]]=True
                                rooms[cur[0]+d[0]][cur[1]+d[1]]=min(rooms[cur[0]+d[0]][cur[1]+d[1]],steps+1)
                                q.append([(cur[0]+d[0],cur[1]+d[1]),steps+1])
        
        return rooms

def wallsAndGates2(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m,n=len(rooms),len(rooms[0])
        dirs=[[-1,0],[1,0],[0,-1],[0,1]]
        
        q=deque()
        
        visited=[[False]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    q.append([(i,j),0])
                    
        while len(q)>0:
            cur,steps=q.popleft()
            for d in dirs:
                if 0<=cur[0]+d[0]<m and 0<=cur[1]+d[1]<n and rooms[cur[0]+d[0]][cur[1]+d[1]]>0 and visited[cur[0]+d[0]][cur[1]+d[1]]==False:
                    visited[cur[0]+d[0]][cur[1]+d[1]]=True
                    rooms[cur[0]+d[0]][cur[1]+d[1]]=steps+1
                    q.append([(cur[0]+d[0],cur[1]+d[1]),steps+1])
        
        return rooms