# given an m x n grid of character board and a string word, return true if word exists in the grid.
# the word can be constructed from letters of sequentially adjacent cells,
#  where adjacent cells are horizontally or vertically neigbouring or vertically neighbouring
# The same letter cell may not be used more than once
def wordSearchII(board: list[list[str]], word: str):
    ROWS = len(board)
    COLS = len(board[0])

    path = set()

    def dfs(r, c, idx):
        if idx == len(word):
            return True

        if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[idx] != board[r][c] or (r, c) in path):
            return False

        path.add((r,c))
        res = ( dfs(r+1, c , idx+1) or 
                dfs(r-1, c , idx+1) or
                dfs(r, c+1 , idx+1) or
                dfs(r, c-1 , idx+1) ) 

        path.remove((r, c))
        return res


    for row in range(ROWS):
        for col in range(COLS):
            if dfs(row, col, 0): return True
    return False

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

print(wordSearchII(board, word))

