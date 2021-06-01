class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def checkBit(n) -> int:
            ans = 0
            while n>0:
                if n%2 ==1:
                    ans+=1
                n//=2
            return ans
        Mydict=[]
        for elem in arr:
            Mydict.append([checkBit(elem),elem])
        Mydict=sorted(Mydict, key=lambda x:(x[0],x[1]))
        ans=[]
        for elem in Mydict:
            ans.append(elem[1])
        return ans
