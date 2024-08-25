from test import test
from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        operations_required = 0

        for operation in logs:
            if operation == "../":
                operations_required = max(0, operations_required - 1)
            elif operation == "./":
                continue
            else:
                operations_required += 1
        return operations_required


if __name__ == "__main__":
    test_cases = {
        "Test 1": {
            "args": (["d1/","d2/","../","d21/","./"],),
            "kwargs": {},
            "answer": 2
        },
        "Test 2": {
            "args": (["d1/","d2/","./","d3/","../","d31/"],),
            "kwargs": {},
            "answer": 3
        },
        "Test 3": {
            "args": (["d1/","../","../","../"],),
            "kwargs": {},
            "answer": 0
        },
    }
    test(Solution().minOperations, test_cases)