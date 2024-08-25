from test import test
from typing import List


class Solution:
    def numTeams_tl(self, rating: List[int]) -> int:
        # Time limit exceeded ...
        ans, n = 0, len(rating)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    ans += 1 if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k] else 0
        return ans
    
    def numTeams(self, rating: List[int]) -> int:
        ans, n = 0, len(rating)

        for j in range(n):
            llt, lgt = 0, 0

            for i in range(j):
                llt += rating[i] < rating[j]
                lgt += rating[i] > rating[j]

            rlt,rgt = 0,0

            for k in range(j + 1, n):
                rlt += rating[k] < rating[j]
                rgt += rating[k] > rating[j]

            ans += llt * rgt + lgt * rlt 

        return ans


if __name__ == "__main__":
    test_cases = {
        "Test 1": {
            "args": (),
            "kwargs": {"rating": [2,5,3,4,1]},
            "answer": 3
        },
        "Test 2": {
            "args": (),
            "kwargs": {"rating": [2,1,3]},
            "answer": 0
        },
        "Test 3": {
            "args": (),
            "kwargs": {"rating": [1,2,3,4]},
            "answer": 4
        },
    }
    
    test(Solution().numTeams, test_cases)