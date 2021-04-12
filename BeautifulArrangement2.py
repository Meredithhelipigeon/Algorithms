class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans=[]
        odd=True
        for i in range(1,n+1):
            if i <= k:
                if odd:
                    odd=False
                    ans.append(i//2+1)
                else:
                    odd=True
                    ans.append(n-i//2+1)
            else:
                if odd:
                    ans.append(ans[-1]-1)
                else:
                    ans.append(ans[-1]+1)
        return ans
