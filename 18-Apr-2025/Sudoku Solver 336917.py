# Problem: Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + j // 3].add(val)
                else:
                    empty.append((i, j))

        def backtrack(idx):
            if idx == len(empty):
                return True

            i, j = empty[idx]
            box_idx = (i // 3) * 3 + j // 3

            for num in map(str, range(1, 10)):
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_idx]:
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_idx].add(num)

                    if backtrack(idx + 1):
                        return True

                    board[i][j] = '.' 
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_idx].remove(num)

            return False

        backtrack(0)




            

        