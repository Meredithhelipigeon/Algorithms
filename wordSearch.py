class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m=len(board)
        n=len(board[0])
        
        def search(i,j,c):
            if c==len(word):
                return True
            if not (0<=i<=m-1 and 0<=j<=n-1):
                return False
            if not board[i][j]==word[c]:
                return False
            if board[i][j]=='':
                return False
            dir=[[0,1],[0,-1],[1,0],[-1,0]]
            ret=False
            temp=board[i][j]
            board[i][j]=''
            for dd in dir:
                if search(i+dd[0],j+dd[1],c+1):
                    ret=True
                    break
            board[i][j]=temp
            return ret
        
        ret=False
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if search(i,j,0):
                        ret=True
                        break
        return ret
