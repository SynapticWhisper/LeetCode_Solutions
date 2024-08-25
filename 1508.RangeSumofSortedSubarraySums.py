from typing import List
from test import test


class Solution:
    MODULO = 10 ** 9 + 7
    # Too long
    def rangeSum_1(self, nums: List[int], n: int, left: int, right: int) -> int:
        result: list = []
        for start in range(n):
            for end in range(start, n):
                result.append(sum(nums[start:end+1]))
        result = sorted(result)
        return sum(result[left-1:right]) % self.MODULO

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        result: list = []

        def merge(left_array: list, right_array: list) -> list:
            i, j = 0, 0
            merged_list = []
            for _ in range(len(left_array) + len(right_array)):
                if i >= len(left_array):
                    merged_list.extend(right_array[j:])
                    break
                elif j >= len(right_array):
                    merged_list.extend(left_array[i:])
                    break
                if left_array[i] >= right_array[j]:
                    merged_list.append(right_array[j])
                    j += 1
                else:
                    merged_list.append(left_array[i])
                    i += 1
            return merged_list
        
        last_sum = [sum(nums[:end+1]) for end in range(n)]
        for num in nums:
            pre_result = list(map(lambda x: x - num, last_sum[1:]))
            # result = merge(result, last_sum)
            result.extend(last_sum)
            last_sum, pre_result = pre_result, []
        
        result.sort()

        return sum(result[left-1:right]) % self.MODULO


test_cases = {
    "Test 1": {
        "args": (),
        "kwargs": {"nums": [1,2,3,4], "n": 4, "left": 1, "right": 5},
        "answer": 13
    },
    "Test 2": {
        "args": (),
        "kwargs": {"nums": [1,2,3,4], "n": 4, "left": 3, "right": 4},
        "answer": 6
    },
    "Test 3": {
        "args": (),
        "kwargs": {"nums": [1,2,3,4], "n": 4, "left": 1, "right": 10},
        "answer": 50
    },
}

if __name__ == "__main__":
    test(Solution().rangeSum, test_cases)