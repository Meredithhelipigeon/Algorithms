class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ret = 0
        nums = sorted(nums)
        # two pointer      
        def twoSumSmaller(start,t):
            ans=0
            end = len(nums) - 1
            while start < end:
                if nums[start]+nums[end] >= t:
                    end-=1
                else:
                    ans+=end-start
                    start+=1
            return ans
        
        for i in range(0,len(nums)-1):
            add=twoSumSmaller(i+1,target-nums[i])
            if add == 0:
                return ret
            else:
                ret+=add
        
        return ret
                
        
