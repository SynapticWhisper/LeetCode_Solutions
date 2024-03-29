class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        maximum_value = max(nums)
        n = len(nums)
        indexes = [index for index, num in enumerate(nums) if num == maximum_value]
        
        if len(indexes) < k:
            return 0

        indexes.insert(0, -1)

        result = 0
        
        for i in range(1, len(indexes) - k + 1):
            l = indexes[i] - indexes[i - 1] - 1
            r = n - 1 - indexes[i + k - 1]
            result += (l + 1) * (r + 1)
            
        return result
    
    
if __name__ == "__main__":
    print(Solution().countSubarrays([61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82], 2))