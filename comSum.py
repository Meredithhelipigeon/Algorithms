class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates=sorted(candidates)
        dp=[[[] for i in range(len(candidates))] for j in range(target)]
        
        for i in range(target):
            for j in range(len(candidates)-1,-1,-1):
                if i+1==candidates[j]:
                    dp[i][j]=[[candidates[j]]]
                elif i+1<candidates[j]:
                    continue
                else:
                    ad=[]
                    if i-candidates[j]>=0:
                        for alist in dp[i-candidates[j]][j]:
                            alist=copy.deepcopy(alist)
                            alist.append(candidates[j])
                            ad.append(alist)
                    dp[i][j]+=ad
                    if j+1< len(candidates):
                        dp[i][j]+=dp[i][j+1]

        return dp[-1][0]
