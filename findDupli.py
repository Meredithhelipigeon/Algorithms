class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        
        for nn in nums:
            if nums[abs(nn)-1]>0:
                nums[abs(nn)-1]*=-1
            else:
                ans.append(abs(nn))
        
        return ans
