class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ourDict={}
        ourDict[0]=1
        cur=0
        ret=0
        
        for nn in nums:
            cur+=nn
            if cur-k in ourDict:
                ret+=ourDict[cur-k]
            if cur in ourDict:
                ourDict[cur]+=1
            else:
                ourDict[cur]=1
        
        return ret
