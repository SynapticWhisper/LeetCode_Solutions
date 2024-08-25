from typing import List
from test import test

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        result.extend(matrix.pop(0))
        
        while len(matrix) > 1:
            matrix = list(zip(*matrix))[::-1]
            result.extend(matrix.pop(0))
        
        if len(matrix) > 0:
            result.extend(matrix.pop()[::-1])
        return result



test_cases = {
    "Test 1": {
        "args": (),
        "kwargs": {"matrix": [[1,2,3],[4,5,6],[7,8,9]]},
        "answer": [1,2,3,6,9,8,7,4,5]
    },
    "Test 2": {
        "args": (),
        "kwargs": {"matrix": [[1,2,3,4],[5,6,7,8],[9,10,11,12]]},
        "answer": [1,2,3,4,8,12,11,10,9,5,6,7]
    },
    "Test 3": {
        "args": (),
        "kwargs": {"matrix": [[7],[9],[6]]},
        "answer": [7, 9, 6]
    },
    "Test 4": {
        "args": (),
        "kwargs": {"matrix": [[1]]},
        "answer": [1]
    },
}

if __name__ == "__main__":
    test(Solution().spiralOrder, test_cases)