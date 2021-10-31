class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.arr=[0]
        cur=0
        for ww in w:
            cur+=ww
            self.arr.append(cur)
        self.weightLen=sum(w)
        

    def pickIndex(self):
        """
        :rtype: int
        """ 
        # Step 1. choose a number in [0,self.weightLen-1] 0,5: 4 [1,2,3]
        randomChoose=randint(1, self.weightLen)
        
        # Step 2.locate this number in self.arr
        ret=bisect_left(self.arr,randomChoose)
        return ret-1
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
