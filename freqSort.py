class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
            
        h=[]
        dic={}
        ret=""
        
        for ss in s:
            if ss in dic:
                dic[ss]+=1
            else:
                dic[ss]=1
        
        for key in dic:
            heappush(h,[-dic[key],key])
        
        while len(h)>0:
            cur=heappop(h)
            ret+=cur[1]*(-cur[0])
            
        return ret
