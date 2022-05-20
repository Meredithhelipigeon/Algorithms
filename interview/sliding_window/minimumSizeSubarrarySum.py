# left, right
# Time complexity: O(n)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curSum=0
        l=0
        r=0
        ret=float('inf')
        
        while r < len(nums):
            curSum+=nums[r]
            while curSum>=target:
                ret=min(ret,r-l+1,curSum)
                curSum-=nums[l]
                l+=1
            r+=1

        if ret==float('inf'): return 0
        return ret
            
