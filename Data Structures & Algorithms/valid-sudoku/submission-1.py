class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for col in range(9):
            seen=set()
            for i in range(9):
                if board[col][i] == ".":
                    continue
                elif board[col][i] in seen:
                    return False
                seen.add(board[col][i])
        for row in range(9):
            seen= set()
            for i in range(9):
                if board[i][row] ==".":
                    continue
                elif board[i][row] in seen:
                    return False
                seen.add(board[i][row])
        for box in range(9):
            seen=set()
            for i in range(3):
                for j in range(3):
                    col = (box%3)*3 + j
                    row = (box//3) * 3 + i 
                    if board[row][col] ==".":
                        continue
                    elif board[row][col] in seen:
                        return False
                    seen.add(board[row][col])      
        return True             
        