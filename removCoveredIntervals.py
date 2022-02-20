class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        curMax=float('-inf')
        intervals=sorted(intervals,key=lambda x: (x[0],-x[1]))
        ret=len(intervals)
        
        for i in intervals:
            l,r=i
            if curMax >= r:
                ret-=1
            else:
                curMax=r
        return ret
