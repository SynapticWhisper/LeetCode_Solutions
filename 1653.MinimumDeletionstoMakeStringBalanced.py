from test import test


class Solution:
    def minimumDeletions(self, s: str) -> int:
        result = 0
        b_count = 0
        for letter in s:
            if letter == 'b':
                b_count += 1
            else:
                result = min(result + 1, b_count)
        return result


if __name__ == "__main__":
    test_cases = {
        "Test 1": {
            "args": (),
            "kwargs": {"s": "aababbab"},
            "answer": 2
        },
        "Test 2": {
            "args": (),
            "kwargs": {"s": "bbaaaaabb"},
            "answer": 2
        }
    }
    test(Solution().minimumDeletions, test_cases)