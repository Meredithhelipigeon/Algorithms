class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        mapper={}
        for i in range(len(order)):
            mapper[order[i]]=chr(ord('a')+i)
        
        newWords=[]
        for w in words:
            newW=""
            for i in range(len(w)):
                newW+=mapper[w[i]]
            newWords.append(newW)
          
        for i in range(0,len(newWords)-1):
            if newWords[i]>newWords[i+1]:
                return False
        return True
