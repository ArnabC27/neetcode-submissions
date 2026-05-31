class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for row_idx in range(9):
            for col_idx in range(9):
                if board[row_idx][col_idx] == ".":
                    continue

                if (board[row_idx][col_idx] in rows[row_idx] or
                    board[row_idx][col_idx] in cols[col_idx] or
                    board[row_idx][col_idx] in boxes[(row_idx // 3, col_idx // 3)]
                    ):
                    return False

                rows[row_idx].add(board[row_idx][col_idx])
                cols[col_idx].add(board[row_idx][col_idx])
                boxes[(row_idx // 3, col_idx // 3)].add(board[row_idx][col_idx])

        return True
