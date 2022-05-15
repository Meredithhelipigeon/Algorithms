# To aviod the situation that it has several duplicate prefix, we use a set.
# By mathematical induction :), we know that if we don't have duplicate prefix,
# we will not have duplicate results
class Solution1(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        last=len(nums)-1
        ret=[]
        
        def permutation(cur,l):
            if cur==last:
                ret.append(l[:])
            curSet = set()
            for i in range(last-cur+1):
                if l[i+cur] not in curSet:
                    l[i+cur],l[cur]=l[cur],l[i+cur]
                    permutation(cur+1,l)
                    l[i+cur],l[cur]=l[cur],l[i+cur]
                    curSet.add(l[i+cur])
        
        permutation(0,nums)
        return ret

