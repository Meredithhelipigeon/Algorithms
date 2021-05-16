class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        while n/3 > 0:
            if n%3==0:
                if n/3 == 1:
                    return True
                else:
                    n=n/3
            else:
                return False
        return False
