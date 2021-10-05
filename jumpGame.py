#         dp=['-inf']*len(nums)
#         dp[-1]=True
        
#         for i in range(len(nums)):
#             if nums[i]>=len(nums)-1-i:
#                 dp[i]=True
            
            
#         for i in range(len(nums)-2,-1,-1):
#             if dp[i]=='-inf':
#                 dp[i]=False
#                 if nums[i]>0:
#                     for j in range(1,nums[i]+1):
#                         if i+j<len(nums) and dp[i+j]==True:
#                             dp[i]=True
#                             break
#         return dp[0]
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxL=1
        index=0
        n=len(nums)
        
        while index < maxL and index < len(nums):
            if maxL>=n:
                return True
            if index+nums[index]+1>maxL:
                maxL=index+nums[index]+1
            index+=1
            
        return maxL>=n