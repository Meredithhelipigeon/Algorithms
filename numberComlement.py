class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = num.bit_length()
        return 2**n-1-num
