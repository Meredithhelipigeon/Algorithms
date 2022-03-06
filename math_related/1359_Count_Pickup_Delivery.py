class Solution1(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = 1
        # First figure the permuatation of P
        for i in range(1,n+1):
            base*=i
        
        m = 10**9+7
        # Then start to calculate the the permuation of D base on P
        for i in range(1,2*n+1,2):
            base *= i 
            if base > m:
                base %= m
            
        return base

# Use the permutation and combination theory to add one (P, D) pair each time until n pairs.
class Solution2(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = 1
        m = 10**9+7
        for i in range(2,n+1):
            base *= i*(2*i-1)
            base %= m
        return base