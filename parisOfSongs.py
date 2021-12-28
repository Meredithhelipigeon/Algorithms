class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        for i in range(len(time)):
            time[i]%=60
        temp={}
        
        for t in time:
            if t in temp:
                temp[t]+=1
            else:
                temp[t]=1
        
        ret=0
        for key in temp:
            if key==30 or key==0:
                ret+=temp[key]*(temp[key]-1)
            elif 60-key in temp:
                ret+=temp[key]*temp[60-key]

        return ret/2
    
    # could update while storing => shorten the code length
    def numPairsDivisibleBy60_V2(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        remainders = [0]*60
        ret=0
        
        for tt in time:
            if tt%60 == 0:
                ret+=remainders[tt%60]
            else:
                ret+=remainders[60-tt%60]
            remainders[tt%60]+=1
        
        return ret
