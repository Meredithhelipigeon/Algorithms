class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minArr = [float('inf')]*len(nums)
        maxArr = [float('-inf')]*len(nums)
        curMin = float('inf')
        curMax = float('-inf')
        
        for i in range(len(nums)-1):
            curMin=min(curMin,nums[len(nums)-i-1])
            minArr[len(nums)-i-2]=curMin
            curMax=max(curMax,nums[i])
            maxArr[i+1]=curMax
        
        start = -1
        end = -1
        
        for i in range(len(nums)):
            if (nums[i]>minArr[i] or nums[i]<maxArr[i]) and start==-1:
                start=i
            if (nums[len(nums)-1-i]>minArr[len(nums)-1-i] or nums[len(nums)-1-i]<maxArr[len(nums)-1-i]) and end==-1:
                print(minArr[len(nums)-1-i])
                print(maxArr[len(nums)-1-i])
                end=len(nums)-1-i
        
        if start==end:
            return 0

        return end-start+1
