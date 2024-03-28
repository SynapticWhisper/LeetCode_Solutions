from collections import defaultdict

# class Solution:
#     def maxSubarrayLength(self, nums: list[int], k: int) -> int:
#         unique = set(nums)
#         values: dict = {uniq: [] for uniq in unique}
#         sub_max = 0
#         counter = 0
#         for index, num in enumerate(nums):
#             values[num].append(index)
#             if len(values[num]) <= k:
#                 counter += 1
#             else:
#                 sub_max = counter if counter > sub_max else sub_max
#                 new_start = values[num].pop(0)
#                 for uniq in unique:
#                     values[uniq] = [i for i in values[uniq] if i > new_start]
#                 counter = index - new_start
#         return sub_max if sub_max > counter else counter
    

class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        ans = left = 0
        counts = defaultdict(int)

        for right in range(len(nums)):
            counts[nums[right]] += 1
            while counts[nums[right]] > k:
                counts[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans
                
                


if __name__ == "__main__":
    Solution().maxSubarrayLength([2, 2, 3], 1)