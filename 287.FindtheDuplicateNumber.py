class Solution1:
    def findDuplicate(self, nums: list[int]) -> int:
        values: dict = {}
        for num in nums:
            count = values.get(num, 0)
            count += 1
            if count > 1:
                return num
            values[num] = count
            
class Solution2:
    def findDuplicate(self, nums: list[int]) -> int:
        
        for num in nums:
            idx = abs(num)
            if nums[idx] < 0:
                return idx
            nums[idx] =  -nums[idx]
        return len(nums)  