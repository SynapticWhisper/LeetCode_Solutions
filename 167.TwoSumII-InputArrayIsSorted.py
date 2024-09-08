from typing import List


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, len(numbers) - 1
        
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1


if __name__ == "__main__":
    Solution().twoSum([0,0,3,4], 0)