class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = [[[0,0] for i in range(len(matrix[0]))] for j in range(len(matrix))]
        rowNum = len(matrix[0])
        colNum = len(matrix)
        ans = []
        print(ret[4][1])
        
        for m in range(len(matrix)):
            print(ret)
            stackP = []
            stackA = []
            for n in range(len(matrix[0])):
                print(ret)
                # Pacific
                if len(stackP)==0 or stackP[-1] <= matrix[m][n] :
                    stackP.append(matrix[m][n])
                    ret[m][n][0] = 1
                # Atlantic
                if len(stackA)==0 or stackA[-1] <= matrix[m][rowNum-1-n] :
                    stackA.append(matrix[m][rowNum-1-n])
                    print(rowNum-1-n)
                    ret[m][rowNum-1-n][1] = 1

        for n in range(len(matrix[0])):
            stackP = []
            stackA = []
            for m in range(len(matrix)):
                # Pacific
                if len(stackP)==0 or stackP[-1] <= matrix[m][n] :
                    stackP.append(matrix[m][n])
                    ret[m][n][0] = 1
                # Atlantic
                if len(stackA)==0 or stackA[-1] <= matrix[colNum-1-m][n] :
                    stackA.append(matrix[colNum-1-m][n])
                    ret[colNum-1-m][n][1] = 1
                if ret[m][n] == [1,1]:
                    ans.append([m,n])
                
        return ans
