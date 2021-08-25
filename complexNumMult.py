class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        index1=num1.find("+")
        r1=int(num1[:index1])
        i1=int(num1[index1+1:-1])
        index2=num2.find("+")
        r2=int(num2[:index2])
        i2=int(num2[index2+1:-1])
        
        rret=r1*r2-i1*i2
        iret=r1*i2+i1*r2
        
        return str(rret)+"+"+str(iret)+"i"
