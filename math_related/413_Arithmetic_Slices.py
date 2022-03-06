class Solution1(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        ret = 0
        for i in range(1,len(nums)):
            if i<len(nums)-1 and nums[i]-nums[i-1]==nums[i+1]-nums[i]:
                cur+=1
            else:
                if cur:
                    l = cur+2
                    ret += (l*(l-1))/2 - (l-1)
                cur=0
        return ret

#  dp[i] denotes the number of slicing sets through 0-i
class Solution2(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = 0
        cur = 0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                cur+=1
                dp += cur
            else:
                cur=0
        return dp
