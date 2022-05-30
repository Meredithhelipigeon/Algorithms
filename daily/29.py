class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ret=0
        mult=1
        if not ((dividend>0 and divisor>0) or (dividend<0 and divisor<0)):
            mult*=-1
            
        dividend=abs(dividend)
        divisor=abs(divisor)
        cur = divisor
        
        while dividend >= divisor:
            add_on = 1
            while cur<dividend:
                add_on = add_on << 1
                cur = cur << 1
            if cur==dividend:
                ret+=add_on
                break
            else:
                add_on=add_on >> 1
                cur=cur >> 1
                ret+=add_on
                dividend-=cur
                cur=divisor
        
        ret*=mult
        
        if ret > 2147483647:
            return 2147483647
        elif ret < -2147483648:
            return -2147483648
        else:
            return ret
