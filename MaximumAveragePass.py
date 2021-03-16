class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        OwnList = [(-1.0*(b-a)/((b+1)*b), a, b) for a,b in classes]
        heapify(OwnList)
        for i in range(extraStudents):
            v, a, b = heappop(OwnList)
            heappush(OwnList,(-1.0*(b-a)/((b+1)*(b+2)), a+1, b+1))
        return sum(1.0*k[1]/k[2] for k in OwnList)/len(classes)

