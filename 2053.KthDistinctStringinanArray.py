from test import test
from typing import List
from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counted = Counter(arr)
        result = [key for key, value in counted.items() if value == 1]
        return result[k-1] if len(result) >= k else ""
        
test_cases = {
    "TEST 1": {
        "args": (),
        "kwargs": {"arr": ["d","b","c","b","c","a"], "k": 2},
        "answer": "a"
    },
    "TEST 2": {
        "args": (),
        "kwargs": {"arr": ["aaa","aa","a"], "k": 1},
        "answer": "aaa"
    },
    "TEST 3": {
        "args": (),
        "kwargs": {"arr": ["a","b","a"], "k": 3},
        "answer": ""
    },
}

if __name__ == "__main__":
    test(Solution().kthDistinct, test_cases)