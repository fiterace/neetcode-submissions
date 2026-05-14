class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import numpy as np
        board = np.array(board)

        def check_rows():
            for board_row in board:
                new_set = set()
                for stuff in board_row:
                    if stuff in new_set and stuff != '.':
                        return False
                    new_set.add(stuff)
            return True

        def check_cols():
            for board_cols in board.T:
                new_set = set()
                for stuff in board_cols:
                    if stuff in new_set and stuff != '.':
                        return False
                    new_set.add(stuff)
            return True
        
        def check_boxes():
            for i in [0,1,2]:
                for j in [0,1,2]:
                    new_set = set()
                    for k in [0,1,2]:
                        for l in [0,1,2]:
                            stuff = board[3*i + k][3*j + l]
                            if stuff in new_set and stuff != '.':
                                return False
                            new_set.add(stuff)  
            return True
        
        return check_rows() and check_cols() and check_boxes()
        