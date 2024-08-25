from typing import List
from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        filtered = sorted([item for item in candidates if item <= target])
        counted = Counter(filtered)

        result = []

        for item in filtered:
            pre_result = target - item
            if counted.get(pre_result, None) is not None:
                result.append


test_cases = {
    "Test 1": {
        "args": (),
        "kwargs": {"candidates": [10,1,2,7,6,1,5], "target": 8},
        "answer": [[1,1,6], [1,2,5], [1,7], [2,6]]
    }
}