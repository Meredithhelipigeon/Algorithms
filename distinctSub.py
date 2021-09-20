class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp=[['-inf']*len(t) for i in range(len(s))]
        
        def cal(sIndex,tIndex):
            if tIndex == len(t):
                return 1
            if sIndex == len(s):
                return 0
            if dp[sIndex][tIndex] != '-inf':
                return dp[sIndex][tIndex]
            if s[sIndex]==t[tIndex]:
                dp[sIndex][tIndex]=cal(sIndex+1,tIndex+1)+cal(sIndex+1,tIndex)
            else:
                dp[sIndex][tIndex]=cal(sIndex+1,tIndex)
            return dp[sIndex][tIndex]
                
        return cal(0,0)
