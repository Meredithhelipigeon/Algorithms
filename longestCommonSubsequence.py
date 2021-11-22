class Solution:
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        self.memerization=[[float('inf')]*len(text2) for i in range(len(text1))]
        def find_max(index1,index2):
            if index1<len(text1) and index2<len(text2):
                if self.memerization[index1][index2]!=float('inf'):
                    return self.memerization[index1][index2]
                if text1[index1]==text2[index2]:
                    ret=max(find_max(index1+1,index2),find_max(index1,index2+1),1+find_max(index1+1,index2+1))
                    self.memerization[index1][index2]=ret
                else:
                    ret=max(find_max(index1+1,index2),find_max(index1,index2+1))
                    self.memerization[index1][index2]=ret
                return ret
            else:
                return 0
            
        ret=find_max(0,0)
        return ret
    
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        dp=[[0]*(len(text2)+1) for i in range(len(text1)+1)]
            
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                        dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
