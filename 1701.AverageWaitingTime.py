from test import test
from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_time: float = 0.0
        now = 1

        for arrival, time in customers:
            tmp = time
            if arrival < now:
                tmp += now - arrival
            else:
                now = arrival
            now += time
            total_time += tmp
        
        return total_time / len(customers)


if __name__ == "__main__":
    test_cases = {
        "Test 1": {
            "args": ([[1,2],[2,5],[4,3]],),
            "kwargs": {},
            "answer": 5.0
        },
        "Test 2": {
            "args": ([[5,2],[5,4],[10,3],[20,1]],),
            "kwargs": {},
            "answer": 3.25
        },
    }
    test(Solution().averageWaitingTime, test_cases)