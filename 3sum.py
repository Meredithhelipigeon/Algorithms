class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(start,end,target):
            ret=[]
            initialStart=start
            while start<end:
                if nums[start]+nums[end]==target:
                    if not (start>initialStart and nums[start-1]==nums[start]):
                        ret.append([nums[start],nums[end]])
                    start+=1
                elif nums[start]+nums[end]<target:
                    start+=1
                else:
                    end-=1
            return ret
        last=float('inf')
        ret=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            if not last==nums[i]:
                pairs=twoSum(i+1,len(nums)-1,-nums[i])
                for p in pairs:                                      
                    ret.append([nums[i]]+p)
            last=nums[i]
        return ret
