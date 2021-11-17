class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        print(len(edges))
        return -1
        #  create an edge Matrix
        edgesMatrix=[[0]*n for i in range(n)]
        hashM = [0]*n
        for e in edges:
            edgesMatrix[e[0]-1][e[1]-1]=1
            edgesMatrix[e[1]-1][e[0]-1]=1
            hashM[e[0]-1]+=1
            hashM[e[1]-1]+=1
        
        #  Mij>1 Eip*Epj=1
        ret=float('inf')
        for i in range(n):
            for j in range(n):
                if edgesMatrix[i][j]==1 and hashM[i]>=2 and hashM[j]>=2:
                    for p in range(n):
                        if edgesMatrix[i][p]*edgesMatrix[j][p]>0:
                            ret=min(ret,hashM[i]+hashM[j]+hashM[p]-6)
                            if ret==0:
                                return 0
                            
        if ret==float('inf'):
            return -1
        return ret

    def minTrioDegree1(self, n: int, edges: List[List[int]]) -> int:
        adjList=[set() for i in range(n)] 
        numList=[0 for i in range(n)]
        
        for e in edges:
            numList[e[0]-1]+=1
            numList[e[1]-1]+=1
            adjList[e[0]-1].add(e[1]-1)
            adjList[e[1]-1].add(e[0]-1)
        
        ret=float('inf')
        for i in range(n):
            for v in adjList[i]:
                if i<=v:
                    continue
                for p in adjList[v]:
                    if v<=p:
                        continue
                    if i not in adjList[p]:
                        continue
                    ret=min(ret,numList[p]+numList[i]+numList[v]-6)
                    
        return -1 if ret==float('inf') else ret
    
    