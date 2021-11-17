class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            visited_row=[0]*9
            visited_col=[0]*9
            for j in range(9):
                if board[i][j]!=".":
                    if "1"<=board[i][j]<="9" and visited_row[int(board[i][j])-1]==0:
                        visited_row[int(board[i][j])-1]+=1
                    else:
                        return False
                if board[j][i]!=".":
                    if "1"<=board[j][i]<="9" and visited_col[int(board[j][i])-1]==0:
                            visited_col[int(board[j][i])-1]+=1
                    else:
                        return False
        
        for i in range(9):
            left_top=[0,0]
            left_top[0]=(i%3)*3
            left_top[1]=(i//3)*3
            visited_cell=[0]*9
            for p in range(3):
                for q in range(3):
                    if board[p+left_top[0]][q+left_top[1]]!=".":
                        if visited_cell[int(board[p+left_top[0]][q+left_top[1]])-1]==0:
                            visited_cell[int(board[p+left_top[0]][q+left_top[1]])-1]+=1
                        else:
                            return False
        return True
