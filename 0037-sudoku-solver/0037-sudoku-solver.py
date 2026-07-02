class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [[0]*9 for _ in range(9)]
        cols = [[0]*9 for _ in range(9)]
        grids = [[0]*9 for _ in range(9)]

        # initial scan
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = int(board[r][c]) - 1
                    g = (r // 3) * 3 + (c // 3)
                    rows[r][num] = 1
                    cols[c][num] = 1
                    grids[g][num] = 1

        # build hash table of empty cells with their candidates
        candidates = {}
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    g = (r // 3) * 3 + (c // 3)
                    valid = []
                    for num in range(9):
                        if rows[r][num] == 0 and cols[c][num] == 0 and grids[g][num] == 0:
                            valid.append(num)
                    candidates[(r, c)] = valid

        def backtrack():
            if not candidates:
                return True

            cell = min(candidates, key=lambda k: len(candidates[k]))
            r, c = cell
            g = (r // 3) * 3 + (c // 3)
            options = candidates.pop(cell)

            for num in options:
                rows[r][num] = 1
                cols[c][num] = 1
                grids[g][num] = 1
                board[r][c] = str(num + 1)

                affected = {}
                for key in list(candidates):
                    kr, kc = key
                    kg = (kr // 3) * 3 + (kc // 3)
                    if kr == r or kc == c or kg == g:
                        if num in candidates[key]:
                            candidates[key].remove(num)
                            affected[key] = num

                if backtrack():
                    return True

                rows[r][num] = 0
                cols[c][num] = 0
                grids[g][num] = 0
                board[r][c] = '.'
                for key, n in affected.items():
                    candidates[key].append(n)

            candidates[cell] = options
            return False

        backtrack()