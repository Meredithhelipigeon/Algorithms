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
