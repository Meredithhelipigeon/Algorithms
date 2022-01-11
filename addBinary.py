class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ret=[]
        last=0
        alen=len(a)-1
        blen=len(b)-1
        for i in range(max(len(a),len(b))):
            if i < len(a) and i < len(b):
                cur=(int(a[alen-i])+int(b[blen-i])+last)%2
                last=(int(a[alen-i])+int(b[blen-i])+last)//2
            elif i<len(a):
                cur=(int(a[alen-i])+last)%2
                last=(int(a[alen-i])+last)//2
            else:
                cur=(int(b[blen-i])+last)%2
                last=(int(b[blen-i])+last)//2
            ret.append(str(cur))
        if last!=0:
            ret.append(str(last))
 
        return "".join(list(reversed(ret)))
    
    def addBinary2(self, a: str, b: str) -> str:
        ret=[]
        last=0
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        for i in range(n-1,-1,-1):
            cur=last
            if a[i]=='1':
                cur+=1
            if b[i]=='1':
                cur+=1
            
            ret.append(str(cur%2))
            last=cur//2
        if last!=0:
            ret.append(str(last))
 
        return "".join(list(reversed(ret)))
