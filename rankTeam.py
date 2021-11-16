class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n=len(votes[0])
        hMap={}
        
        for i in range(n):
            hMap[votes[0][i]]=[0]*n
        
        for v in votes:
            for i in range(len(v)):
                hMap[v[i]][i]+=1
        
        ret=sorted([key for key in hMap],key=lambda x:(hMap[x],-ord(x)))

        return "".join(reversed(ret))
