class Solution:
    def integerBreak(self, n: int) -> int:
        self.remainders = [float('inf')]*n
        self.remainders[0] = 1
        self.remainders[1] = 2
        def recurse_helper(t):
            if self.remainders[t-1]!=float('inf'):
                return self.remainders[t-1]
            ret = 0
            for i in range(1,t):
                ret=max(ret,i*recurse_helper(t-i))
            self.remainders[t-1]=max(t,ret)
            return ret
        if n==2:
            return 1
        ans=recurse_helper(n)
        return ans
