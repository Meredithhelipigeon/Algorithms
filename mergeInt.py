class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals=sorted(intervals)
        cur=intervals[0]
        ret=[]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=cur[1]:
                if cur[1]<intervals[i][1]:
                    cur[1]=intervals[i][1]
            else:
                ret.append(cur)
                cur=intervals[i]
        ret.append(cur)
        return ret
