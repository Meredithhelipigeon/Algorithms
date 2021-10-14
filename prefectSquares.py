# class Solution(object):
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         dp=[float("inf")]*n
#         i=1
#         while i**2<=n:
#             dp[i**2-1]=1
#             i+=1
#         def ourDP(num):
#             if not dp[num-1]==float("inf"):
#                 return dp[num-1]
#             k=sqrt(num)
#             i=1
#             while i < k:
#                 dp[num-1]=min(dp[num-1],1+ourDP(num-i**2))
#                 i+=1
#             return dp[num-1]
#         ourDP(n)
#         return dp[-1]
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        nums=['inf']*n
        
        
        i=1
        cur=[]
        while i**2 <= n:
            nums[i**2-1]=1
            cur.append(i**2)
            i+=1
        
        times=2
        while nums[-1]=='inf':
            l=[]
            for curNum in cur:
                i=1
                while curNum+i**2<=n:
                    if nums[curNum+i**2-1]=='inf':
                        nums[curNum+i**2-1]=times
                        l.append(curNum+i**2)
                    i+=1
            cur=l
            times+=1
                
        return nums[-1]
