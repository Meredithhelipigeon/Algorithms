class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
         # held sold reset        
        dp=[[0,0,0] for i in range(len(prices))]
        
        dp[0][0]=-prices[0]
        dp[0][1]=float('-inf')
        dp[0][2]=0
        
        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][2]-prices[i])
            dp[i][1]=dp[i-1][0]+prices[i]
            dp[i][2]=max(dp[i-1][2],dp[i-1][1])
        
        return max(max(dp[-1]),0)
