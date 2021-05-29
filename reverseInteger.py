class Solution:
    def reverse(self, x: int) -> int:
        positive=True
        if x<0:
            positive = False
            x=-x
        ret=0
        while x>0:
            ret=ret*10+x%10
            if ret >= 2147483647:
                if ret >= 2147483648:
                    return 0
                elif positive==True:
                    return 0
            x//=10
        if positive==False:
            ret*=-1
        return ret
