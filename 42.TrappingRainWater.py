# class Solution:
#     def trap(self, height: list[int]) -> int:
#         mass = []
#         h = max(height)
#         for i in range(1, h+1):
#             value = [1 if x >= i else 0 for x in height]
#             mass.insert(0, value)
#         result = 0
#         for i in range(len(mass)):
#             counter = 0
#             start = None
#             for ind, item in enumerate(mass[i]):
#                 if item == 0 and start is not None:
#                     counter += 1
#                 elif item == 1 and start is not None:
#                     result += counter
#                     counter = 0
#                     start = ind
#                 elif item == 1 and start is None:
#                     start = ind
#                     counter = 0

#         print(result)

# Time Limit Exceeded

# class Solution:
#     def trap(self, height: list[int]) -> int:
#         max_value: int = max(height)
#         result: int = 0
        
#         while max_value > 0:
#             start: bool = False
#             counter: int = 0
#             for item in height:
#                 if item < max_value and start:
#                     counter += 1
#                 elif item >= max_value and start:
#                     result += counter
#                     counter = 0
#                 elif item >= max_value and not start:
#                     start = True
#                     counter = 0
#             max_value -= 1
#         return result

class Solution:
    def trap(self, height: list[int]) -> int:
        i = 0
        left_max = height[0]
        result = 0
        j = len(height) - 1
        right_max = height[j]
        while i < j:
            if left_max <= right_max:
                result += left_max - height[i]
                i += 1
                left_max = max(left_max, height[i])
            else:
                result += right_max - height[j]
                j -= 1
                right_max = max(right_max, height[j])
        return result


if __name__ == "__main__":
    Solution().trap([4,2,0,3,2,5])

