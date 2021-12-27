class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        retList = [0] * length
        for update in updates:
            start,end,inc = update
            retList[start]+=inc
            if end+1 < length:
                retList[end+1]-=inc
        
        temp = 0
        for i in range(length):
            temp += retList[i]
            retList[i]=temp
        return retList
