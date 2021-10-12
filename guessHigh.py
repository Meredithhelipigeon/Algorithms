# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start=1
        end=n
        
        while (not guess((start+end)//2)==0) and start<=end:
            if guess((start+end)//2)==1:
                     start=max(start,(start+end)//2+1)
            else:
                     end=min((start+end)//2,end)
        
        return (start+end)//2
