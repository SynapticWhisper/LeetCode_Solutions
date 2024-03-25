class Solution1:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        cache: dict = {}
        result: list = []
        for i in range(len(nums)):
            value = cache.get(nums[i], 0)
            value += 1
            if value > 1:
                result.append(nums[i])
            cache[nums[i]] = value
        return result
            

class Solution2:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        result = set()
        i = 0
        while i < len(nums):
            num = nums[i]
            if num == i + 1 or num == 0:
                i += 1
            elif num == nums[num - 1]:
                result.add(num)
                nums[i] = 0
                i += 1
            else:
                nums[num - 1], nums[i] = nums[i], nums[num - 1]
        return list(result)

    
if __name__ == "__main__":
    Solution1().findDuplicates([4,3,2,7,8,2,3,1])