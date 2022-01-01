class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        def twoSum(start,target):
            end = len(nums)-1
            ret = []
            while start<end:
                if nums[start]+nums[end]==target:
                    if len(ret)==0 or nums[start]!=ret[-1][0]:
                        ret.append([nums[start],nums[end]])
                    start+=1
                    end-=1
                elif nums[start]+nums[end]<target:
                    start+=1
                else:
                    end-=1
            return ret
        retTuples = []
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                retPairs = twoSum(i+1,0-nums[i])
                for p in retPairs:
                    retTuples.append([nums[i]]+p)
        return retTuples
