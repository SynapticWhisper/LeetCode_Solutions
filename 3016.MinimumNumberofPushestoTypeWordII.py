from test import test
from collections import Counter

class Solution:
    KEYS_COUNT = 8

    def minimumPushes(self, word: str) -> int:
        counted = Counter(word)
        values: list = sorted(counted.values(), reverse=True)
        result = 0
        iteration = 1
        while values:
            i_values, values = values[:self.KEYS_COUNT], values[self.KEYS_COUNT:]
            i_result = sum(i_values) * iteration
            # I dont know what for, but if you want you can do it like this
            # one more unnecessary iteration, but it works correctly xD
            # i_result = sum(map(lambda x: x * iteration, i_values))
            result += i_result
            iteration += 1
        return result


test_cases = {
    "TEST 1": {
        "args": (),
        "kwargs": {"word": "abcde"},
        "answer": 5
    },
    "TEST 2": {
        "args": (),
        "kwargs": {"word": "xyzxyzxyzxyz"},
        "answer": 12
    },
    "TEST 3": {
        "args": (),
        "kwargs": {"word": "aabbccddeeffgghhiiiiii"},
        "answer": 24
    },
}

if __name__ == "__main__":
    test(Solution().minimumPushes, test_cases)