class Solution1(object):
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

class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        last=len(nums)-1
        ret=[]
        
        def permutation(cur,l):
            if cur==last:
                ret.append(l[:])
            for i in range(last-cur+1):
                # swap pos i+cur and pos cur
                l[cur], l[i+cur] = l[i+cur], l[cur]
                permutation(cur+1,l)
                # swap back pos i+cur and pos cur
                l[cur], l[i+cur] = l[i+cur], l[cur]
        
        permutation(0,nums)
        return ret

# Question: Why we use backtracking here? Why not use the simplest method: 
#   know the permutations for indices 0 to i and add index i+1 to permuation list?
# Answer: 