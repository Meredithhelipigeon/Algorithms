class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        ret=0
        
        for nn in nums:
            if nn == 1:
                count+=1
            else:
                if count > ret:
                    ret=count
                count=0
        ret=max(ret,count)
        return ret
