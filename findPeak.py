class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1
        
        start=1
        end=len(nums)-2
        while start< end:
            mid=(start+end)//2
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid
            if nums[mid-1]<nums[mid]<nums[mid+1]:
                start=mid+1
            else:
                end=mid-1
                
        mid=(start+end)//2
        if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
            return mid
        return -1
    
    def findPeakElement2(self, nums: List[int]) -> int:        
        start=0
        end=len(nums)-1
        while start< end:
            mid=(start+end)//2
            if nums[mid]<nums[mid+1]:
                start=mid+1
            else:
                end=mid
            
        return end
