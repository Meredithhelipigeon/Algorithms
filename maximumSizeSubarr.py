class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        
        sub=[0]*len(nums)
        s=0
        ret=0
        hashMap={}
        
        for i in range(n):
            s+=nums[i]
            sub[i]=s
            hashMap[sub[i]]=i
        
        for i in range(n):
            temp=sub[i]
            tt=hashMap.get(temp+k)
            if not tt == None:
                if tt-i > ret:
                    ret=tt-i
            if temp==k and ret<i+1:
                ret=i+1
        
        return ret
