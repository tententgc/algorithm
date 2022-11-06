import itertools
def sudoku(board): 
    rows = board
    columns = [tuple(row[i] for row in rows) for i in range(9)]
    boxes = [tuple(itertools.chain.from_iterable([row[j:j+3] for row in rows[i:i+3]])) for i in (0, 3, 6) for j in (0, 3, 6)]
    
    for group in rows + columns + boxes: 
        if len(set(group) - {'.'}) + group.count('.') != 9: 
            return False
    return True 
    
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(sudoku(board))