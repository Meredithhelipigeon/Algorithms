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

    def pacificAtlanticV3(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = [[[0,0] for i in range(len(matrix[0]))] for j in range(len(matrix))]
        rowNum = len(matrix[0])
        colNum = len(matrix)
        ans = []
        frontierP = []
        frontierA = []
        
        for m in range(len(matrix)):
            frontierP.append([m,0])
            ret[m][0][0]=1
            frontierA.append([m,rowNum-1])
            ret[m][rowNum-1][1]=1
        
        for n in range(len(matrix[0])):
            frontierP.append([0,n])
            ret[0][n][0]=1
            frontierA.append([colNum-1,n])
            ret[colNum-1][n][1]=1
        
        trackC = rowNum
        trackR = colNum
        
        while len(frontierP) != 0 or len(frontierA) != 0:
            if trackC == 1 or trackR == 1:
                break
            NewP = []
            NewA = []
            for p in frontierP:
                if p[1]==rowNum-trackC and p[0] != colNum-trackR:
                    if(matrix[p[0]][p[1]+1]>=matrix[p[0]][p[1]]):
                        NewP.append([p[0],p[1]+1])
                        ret[p[0]][p[1]+1][0]=1
                elif p[0] == colNum-trackR and p[1]!=rowNum-trackC:
                    if(matrix[p[0]+1][p[1]]>=matrix[p[0]][p[1]]):
                        NewP.append([p[0]+1,p[1]])
                        ret[p[0]+1][p[1]][0]=1
            frontierP=NewP
            
            for p in frontierA:
                if p[1]==trackC-1 and p[0] != trackR-1:
                    if(matrix[p[0]][p[1]-1]>=matrix[p[0]][p[1]]):
                        NewA.append([p[0],p[1]-1])
                        ret[p[0]][p[1]-1][1]=1
                elif p[0] == trackR-1 and p[1]!=trackC-1:
                    if(matrix[p[0]-1][p[1]]>=matrix[p[0]][p[1]]):
                        NewA.append([p[0]-1,p[1]])
                        ret[p[0]-1][p[1]][1]=1
            frontierA=NewA
            trackC -= 1
            trackR -= 1
        
        print(ret)
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if ret[m][n]==[1,1]:
                    ans.append([m,n])
        
        return ans

    def pacificAtlanticV2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = [[[0,0] for i in range(len(matrix[0]))] for j in range(len(matrix))]
        rowNum = len(matrix[0])
        colNum = len(matrix)
        ans = []
        frontierP = []
        frontierA = []
        
        for m in range(len(matrix)):
            frontierP.append([m,0])
            ret[m][0][0]=1
            frontierA.append([m,rowNum-1])
            ret[m][rowNum-1][1]=1
        
        for n in range(len(matrix[0])):
            frontierP.append([0,n])
            ret[0][n][0]=1
            frontierA.append([colNum-1,n])
            ret[colNum-1][n][1]=1
        
        while len(frontierP) != 0 or len(frontierA) != 0:
            newP=[]
            newA=[]
            for p in frontierP:
                # up
                if p[0] > 0 and matrix[p[0]-1][p[1]] >= matrix[p[0]][p[1]] and ret[p[0]-1][p[1]][0]!=1:
                    ret[p[0]-1][p[1]][0]=1
                    newP.append([p[0]-1,p[1]])
                # down
                if p[0] < colNum-1 and matrix[p[0]+1][p[1]] >= matrix[p[0]][p[1]] and ret[p[0]+1][p[1]][0]!=1:
                    ret[p[0]+1][p[1]][0]=1
                    newP.append([p[0]+1,p[1]])
                # left
                if p[1] > 0 and matrix[p[0]][p[1]-1] >= matrix[p[0]][p[1]] and ret[p[0]][p[1]-1][0]!=1:
                    ret[p[0]][p[1]-1][0]=1
                    newP.append([p[0],p[1]-1])
                # right
                if p[1] < rowNum-1 and matrix[p[0]][p[1]+1] >= matrix[p[0]][p[1]] and ret[p[0]][p[1]+1][0]!=1:
                    ret[p[0]][p[1]+1][0]=1
                    newP.append([p[0],p[1]+1])
            for p in frontierA:
                # up
                if p[0] > 0 and matrix[p[0]-1][p[1]] >= matrix[p[0]][p[1]] and ret[p[0]-1][p[1]][1]!=1:
                    ret[p[0]-1][p[1]][1]=1
                    newA.append([p[0]-1,p[1]])
                # down
                if p[0] < colNum-1 and matrix[p[0]+1][p[1]] >= matrix[p[0]][p[1]] and ret[p[0]+1][p[1]][1]!=1:
                    ret[p[0]+1][p[1]][1]=1
                    newA.append([p[0]+1,p[1]])
                # left
                if p[1] > 0 and matrix[p[0]][p[1]-1] >= matrix[p[0]][p[1]] and ret[p[0]][p[1]-1][1]!=1:
                    ret[p[0]][p[1]-1][1]=1
                    newA.append([p[0],p[1]-1])
                # right
                if p[1] < rowNum-1 and matrix[p[0]][p[1]+1] >= matrix[p[0]][p[1]] and ret[p[0]][p[1]+1][1]!=1:
                    ret[p[0]][p[1]+1][1]=1
                    newA.append([p[0],p[1]+1])
            frontierA=newA
            frontierP=newP
                    
        
        # print(ret)
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if ret[m][n]==[1,1]:
                    ans.append([m,n])
        
        return ans

    def pacificAtlanticV4(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = [[[0,0] for i in range(len(matrix[0]))] for j in range(len(matrix))]
        rowNum = len(matrix[0])
        colNum = len(matrix)
        ans = []
        
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        
        frontierP = [[0,i] for i in range(rowNum)] + [[i,0] for i in range(colNum)]
        frontierA = [[colNum-1,i] for i in range(rowNum)] + [[i,rowNum-1] for i in range(colNum)]
        
        
        while len(frontierP) != 0 or len(frontierA) != 0:
            newP=[]
            newA=[]
            for p in frontierP:
                ret[p[0]][p[1]][0] = 1
                for d in range(4):
                    if  0 <= p[0]+direction[d][0] < colNum and  0 <= p[1]+direction[d][1] < rowNum and ret[p[0]+direction[d][0]][p[1]+direction[d][1]][0] != 1 and matrix[p[0]+direction[d][0]][p[1]+direction[d][1]] >= matrix[p[0]][p[1]]:
                        newP.append([p[0]+direction[d][0], p[1]+direction[d][1]])
                    
            for p in frontierA:
                ret[p[0]][p[1]][1] = 1
                for d in range(4):
                    if 0 <= p[0]+direction[d][0] < colNum and 0 <= p[1]+direction[d][1] < rowNum and ret[p[0]+direction[d][0]][p[1]+direction[d][1]][1] != 1 and matrix[p[0]+direction[d][0]][p[1]+direction[d][1]] >= matrix[p[0]][p[1]]:
                        newA.append([p[0]+direction[d][0], p[1]+direction[d][1]])
            frontierA=newA
            frontierP=newP
                    
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if ret[m][n]==[1,1]:
                    ans.append([m,n])
        
        return ans