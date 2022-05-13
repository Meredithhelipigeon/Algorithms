class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Get all permutations of nums
        perm = permutations(nums)
        
        ret = []

        for i in list(perm):
            ret.append(list(i))
        
        return ret
