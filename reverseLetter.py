class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp=""
        for ss in s:
            if 'A' <= ss <= 'Z' or 'a' <= ss <= 'z':
                temp+=ss
        
        index=len(temp)-1
        ret=""
        for i in range(len(s)):
            if 'A' <= s[i] <= 'Z' or 'a' <= s[i] <= 'z':
                ret+=temp[index]
                index-=1
            else:
                ret+=s[i]
        
        return ret

class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        index1=0
        index2=len(s)-1
        ret=list(s)
        
        while index1 < len(s):
            while index1<len(s) and not ('A' <= s[index1] <= 'Z' or 'a' <= s[index1] <= 'z'):
                index1+=1
            while index2>=0 and not ('A' <= s[index2] <= 'Z' or 'a' <= s[index2] <= 'z'):
                index2-=1
            if index1 < len(s):
                ret[index1]=s[index2]
                index1+=1
                index2-=1
        
        t=""
        for rr in ret:
            t+=rr
        
        return t
