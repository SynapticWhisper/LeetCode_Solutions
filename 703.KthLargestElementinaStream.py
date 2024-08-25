from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        self.nums = [num for num in self.nums if num <= val] + [val] + [num for num in self.nums if num > val]
        return self.nums[-self.k]
    