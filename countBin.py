class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prefix=[0]*(len(s)+1)
        prefixAction=[0]*(len(s)+1)
        last=s[0]
        cur=0
        curAct=0
        for i in range(1,len(prefix)):
            if s[i-1]=="1":
                cur+=1
            prefix[i]=cur
            if s[i-1]!=last:
                curAct+=1
            prefixAction[i]=curAct
            last=s[i-1]
        
        ret=0
        for i in range(1,len(prefix)):
            for j in range(i+1,len(prefix)):
                if j-i+1==(prefix[j]-prefix[i-1])*2 and prefixAction[j]-prefixAction[i]==1:
                    ret+=1
                    
        return ret

    def countBinarySubstrings2(self, s: str) -> int:
        last=s[0]
        curLast=0
        cur=0
        ret=0
        for ss in s:
            if ss!=last:
                curLast=cur
                cur=0
            cur+=1
            if cur<=curLast:
                ret+=1
            last=ss
        return ret