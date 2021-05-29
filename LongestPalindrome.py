class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret=""
        curNum=0
        stringLen=len(s)
        # if the median is single
        for i in range(len(s)):
            start=i
            end=i
            while start-1>=0 and end+1 < stringLen and s[start-1]==s[end+1]:
                start-=1
                end+=1
            if end-start+1 > curNum:
                curNum=end-start+1
                ret=s[start:end+1]
            if i+1<stringLen and s[i]==s[i+1]:
                start2=i
                end2=i+1
                while start2-1>=0 and end2+1 < stringLen and s[start2-1]==s[end2+1]:
                    start2-=1
                    end2+=1
                if end2-start2+1>curNum:
                    curNum=end2-start2+1
                    ret=s[start2:end2+1]
        
        return ret
