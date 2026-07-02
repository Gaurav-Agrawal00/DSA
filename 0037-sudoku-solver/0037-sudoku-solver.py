class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # N-Queens wala Hashing Magic! 
        # Sets use kar rahe hain taaki O(1) mein check kar sakein
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        
        # STEP 1: Pura board scan karo. 
        # Jo number pehle se hain, unhe Sets mein daal do.
        # Jo khali hain, unhe empty_cells mein daal do.
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    val = board[r][c]
                    box_idx = (r // 3) * 3 + (c // 3)
                    
                    # Sets mein number daal diya
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)
                    
        # STEP 2: Main Backtracking Function
        def backtrack(index):
            # Base Case
            if index == len(empty_cells):
                return True
                
            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)
            
            for val in "123456789":
                # O(1) CHECK - Bina kisi function ya loop ke!
                if val not in rows[r] and val not in cols[c] and val not in boxes[box_idx]:
                    
                    # Tika lagao (Board par aur Sets dono mein)
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)
                    
                    # Recursion
                    if backtrack(index + 1) == True:
                        return True
                        
                    # Backtrack (Tika hatao)
                    board[r][c] = '.'
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[box_idx].remove(val)
                    
            return False
            
        # Function ko call karo
        backtrack(0)