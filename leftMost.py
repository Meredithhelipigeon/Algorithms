# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution1(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        rows,cols=binaryMatrix.dimensions()
        ret=float('inf')
        
        for i in range(rows):
            start=0
            end=cols-1
            if binaryMatrix.get(i,start)==1:
                return 0
            if binaryMatrix.get(i,end)==0:
                continue
            while start<end:
                if end-start==1:
                    break
                mid=(start+end)/2
                if binaryMatrix.get(i,mid)==1:
                    end=mid
                else:
                    start=mid
            if end<ret:
                ret=end
        
        if ret==float('inf'):
            return -1
        return ret

class Solution2(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        rows,cols=binaryMatrix.dimensions()
        ret=float('inf')
        
        for i in range(rows):
            start=0
            end=cols-1
            while start<end:
                mid=(start+end)/2
                if binaryMatrix.get(i,mid)==1:
                    end=mid
                else:
                    start=mid+1
            if end<ret and binaryMatrix.get(i,end)==1:
                ret=end
        
        if ret==float('inf'):
            return -1
        return ret

class Solution3(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        rows,cols=binaryMatrix.dimensions()
        ret=float('inf')
        
        for i in range(rows):
            cur=ret
            for j in range(min(ret,cols-1),-1,-1):
                if binaryMatrix.get(i,j)==1:
                    cur=j
                else:
                    break
            ret=cur
        
        if ret==float('inf'):
            return -1
        return ret