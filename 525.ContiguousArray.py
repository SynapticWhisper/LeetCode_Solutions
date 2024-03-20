class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        sub_max = 0
        counter = 0
        index = 0
        target: set = {1, 0}
        while index < len(nums):
            num_1 = nums[index]
            if index + 1 < len(nums):
                num_2 = nums[index+1]
            else:
                break
            if {num_1, num_2} == target:
                counter += 1
                index += 2
            else:
                sub_max = counter if counter > sub_max else sub_max
                counter = 0
                index += 1
        sub_max = counter if counter > sub_max else sub_max
        return sub_max * 2

if __name__ == "__main__":
    print(Solution().findMaxLength([0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1]))
