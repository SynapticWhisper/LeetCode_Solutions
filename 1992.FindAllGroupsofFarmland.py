from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        cache = set()
        row_count = len(land)
        col_count = len(land[0])
        result = []

        def get_group(row: int, col: int) -> List[int]:
            
            nonlocal cache

            r, c = row, col

            while r + 1 < row_count and land[r+1][c] == 1:
                r += 1

            while c + 1 < col_count and land[r][c+1] == 1:
                c += 1

            for i in range(row, r + 1):
                    for j in range(col, c + 1):
                        cache.add((i, j))
            
            return [row, col, r, c]


        
        for row in range(row_count):
            for col in range(col_count):
                if (row, col) in cache:
                    continue
                if land[row][col] == 0:
                    continue
                result.append(get_group(row, col))

        return result
                

test_case = {
    "test_1": {
        "land": [[1,0,0],[0,1,1],[0,1,1]],
        "answer": {(0,0,0,0),(1,1,2,2)}
    },
    "test_2": {
        "land": [[1,1],[1,1]],
        "answer": {(0,0,1,1)}
    },
    "test_3": {
        "land": [[0]],
        "answer": set()
    }
}

def test_solution():
    for key, value in test_case.items():
        assert len(
            value["answer"] ^ {tuple(x) for x in Solution().findFarmland(value["land"])}
        ) == 0, f"Rong answer {key}"

    

if __name__ == "__main__":
    test_solution()