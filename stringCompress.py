class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        last=chars[0]
        count=1
        delay=0
        
        for i in range(1,len(chars)+1):
            if i<len(chars) and last == chars[i]:
                count+=1
            else:
                if count > 1:
                    cstr=str(count)
                    l=len(cstr)
                    delay+=count-1-l
                    for j in range(l):
                        chars[i-1-delay-j]=cstr[l-1-j]
                    chars[i-1-delay-l]=last
                    count=1
                else:
                    chars[i-1-delay]=last
                if i<len(chars):
                    last=chars[i]
        lenChars=len(chars)
        chars=chars[:lenChars-delay]
        return len(chars)
