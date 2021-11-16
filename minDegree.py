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
