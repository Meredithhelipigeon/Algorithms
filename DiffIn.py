class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        s=""
        ns = ""
        num = set()
        
        for x in word:
            if x >= '0' and x <= '9' :
                if s=='0':
                    s=x
                else:
                    s+=x
            else:
                if len(s) != 0:
                    num.add(s)
                    s=""
                    
        if len(s) != 0:
            num.add(s)
        
        return len(num)
