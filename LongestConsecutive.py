class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        mySet=set(nums)
        ans=1
        for elem in mySet:
            cur=1
            if elem-1 not in mySet:
                while elem+1 in mySet:
                    cur+=1
                    elem+=1
                    if cur > ans:
                        ans = cur
        return ans
