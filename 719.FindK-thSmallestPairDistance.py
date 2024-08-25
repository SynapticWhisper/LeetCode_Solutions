from typing import List
from test import test

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        count_of_i_combination = len(nums) - 1
        first_number_index = 0

        while k > count_of_i_combination and count_of_i_combination >= 1:
            first_number_index += 1
            k -= count_of_i_combination
            count_of_i_combination -= 1
        
        return abs(nums[first_number_index] - nums[first_number_index:][k])


a = [1, 3, 1]
k = 1

# 2, 5
test_cases = {}

if __name__ == "__main__":
    # test(Solution().smallestDistancePair, test_cases)
    Solution().smallestDistancePair(a, k)