class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
            
        h=[]
        dic={}
        ret=[]
        
        for ss in s:
            if ss in dic:
                dic[ss]+=1
            else:
                dic[ss]=1
        
        for key in dic:
            h.append([dic[key],key])
        
        h=sorted(h)
        for i in range(len(h)-1,-1,-1):
            freq=h[i][0]
            c=h[i][1]
            ret.append(c*freq)
            
        return "".join(ret)
