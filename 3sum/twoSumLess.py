class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        start = 0
        end = len(nums)-1
        ret=-1
        
        while start<end:
            if nums[start]+nums[end]>=k:
                end-=1
            else:
                if k-ret>k-(nums[start]+nums[end]):
                    ret = nums[start]+nums[end]
                start+=1
        
        return ret
