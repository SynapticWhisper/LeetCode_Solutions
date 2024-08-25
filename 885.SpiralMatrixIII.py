from test import test
from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        min_row_index, max_row_index = 0, rows - 1
        min_col_index, max_col_index = 0, cols - 1
        cords_count = rows * cols
        result = []
        
        row, col = rStart, cStart
        step = 1


        def check_position(row: int, col: int) -> bool:
            if min_row_index <= row <= max_row_index and min_col_index <= col <= max_col_index:
                return True
            return False
        

        operations = [
            ("col", lambda: col + 1),
            ("row", lambda: row + 1), 
            ("col", lambda: col - 1),
            ("row", lambda: row - 1)]

        result.append([row, col])
        o = 0
        while len(result) < cords_count:
            for _ in range(step):
                row = operations[o][-1]() if operations[o][0] == "row" else row
                col = operations[o][-1]() if operations[o][0] == "col" else col
                if len(result) >= cords_count:
                    break
                if check_position(row, col):
                    result.append([row, col])
            o += 1
            if o > 3:
                o = 0
            if o % 2 == 0:
                step += 1
        return result


test_cases = {
    "Test 1": {
        "args": (),
        "kwargs": {"rows": 1, "cols": 4, "rStart": 0, "cStart": 0},
        "answer": [[0,0],[0,1],[0,2],[0,3]]
    },
    "Test 2": {
        "args": (),
        "kwargs": {"rows": 5, "cols": 6, "rStart": 1, "cStart": 4},
        "answer": [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
    },
}

if __name__ == "__main__":
    test(Solution().spiralMatrixIII, test_cases)