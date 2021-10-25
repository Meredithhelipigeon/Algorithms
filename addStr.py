class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ret=[]
        index=0
        add=False
        l1=len(num1)
        l2=len(num2)
        
        while index<l1 or index<l2:
            cur=0
            if add:
                cur+=1
            if index<l1 and index<l2:
                cur+=int(num1[l1-1-index])+int(num2[l2-1-index])
            elif index<l1:
                cur+=int(num1[l1-1-index])
            else:
                cur+=int(num2[l2-1-index])
            if cur>=10:
                add=True
            else:
                add=False
            ret.append(cur%10)
            index+=1
        if add==True:
            ret.append(1)
        
        ret=[str(i) for i in ret]
        
        return "".join(reversed(ret))
