class Solution:
    def countSubarrays(self, nums: list[int], mink: int, maxK: int) -> int:

        res = 0
        bad_idx = left_idx = right_idx = -1

        for i, num in enumerate(nums) :
            if not mink <= num <= maxK:
                bad_idx = i

            if num == mink:
                left_idx = i

            if num == maxK:
                right_idx = i

            res += max(0, min(left_idx, right_idx) - bad_idx)

        return res
    
if __name__ == "__main__":
    Solution().countSubarrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5)