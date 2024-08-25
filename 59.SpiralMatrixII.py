from typing import List
from test import test

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        values = list(range(1, n**2+1))
        result = [[values.pop()]]

        while values:
            for i in range(len(result)):
                result[i] = [values.pop()] + list(result[i])
            result = [col[::-1] for col in zip(*result)]
        return result


test_cases = {
    "Test 1": {
        "args": (),
        "kwargs": {"n": 3},
        "answer": [[1,2,3],[8,9,4],[7,6,5]]
    },
    "Test 2": {
        "args": (),
        "kwargs": {"n": 1},
        "answer": [[1]]
    },
}

if __name__ == "__main__":
    test(Solution().generateMatrix, test_cases)