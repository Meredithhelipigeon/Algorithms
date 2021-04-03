class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        ret = [[0]*(m+1) for i in range(n+1)]       
        
        for s in strs:
            zeroNum=s.count('0')
            oneNum=s.count('1')
            for i in range(n,oneNum-1,-1):
                for j in range(m,zeroNum-1,-1):
                    ret[i][j]=max(ret[i][j],ret[i-oneNum][j-zeroNum]+1)
                                        
        return ret[n][m]
