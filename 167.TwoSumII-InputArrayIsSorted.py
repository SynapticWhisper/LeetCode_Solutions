class Solution:
    def twoSum_not_toogood(self, numbers: list[int], target: int) -> list[int]:
        indexed_values: dict = {}

        for i, number in enumerate(numbers):
            indexes = indexed_values.get(number, [])
            indexes.append(i)
            indexed_values[number] = indexes

        for i, num in enumerate(numbers):
            tmp = target - num
            indexes = indexed_values.get(tmp, None)
            if not indexes:
                continue
            elif tmp == num and len(indexes) >= 2:
                return list(map(lambda x: x+1, indexes))
            elif tmp == num:
                continue
            else:
                return sorted([i+1, indexes[0]+1])
            

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