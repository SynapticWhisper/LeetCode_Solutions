class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        i = 0
        ans = []

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            interval = intervals[i]
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(interval[1], newInterval[1])
            i += 1
        
        ans.append(newInterval)
        while i < len(intervals):
            ans.append(intervals[i])
            i += 1
        
        return ans



# class Solution:
#     def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

#         h_start = None

#         result = []
        
#         i = 0
#         if not intervals:
#             return [newInterval]
#         while True:
#             if i >= len(intervals):
#                 result.append([h_start, newInterval[-1]])
#                 return result
#             s_i, e_i = [
#                 self.is_in_interval(
#                     intervals[i][0], intervals[i][-1], value
#                 ) for value in newInterval
#             ] 

#             if s_i:
#                 if e_i:
#                     return intervals
#                 else:
#                     h_start = intervals[i][0]
#                     i += 1
            
#             elif newInterval[0] < intervals[i][0]:
#                 if newInterval[-1] < intervals[i][0]:
#                     if h_start is not None:
#                         value = [h_start, newInterval[-1]]
#                     else:
#                         value = newInterval
#                     result.append(value)
#                     result.extend(intervals[i:])
#                     return result
                
#                 elif e_i:
#                     if h_start is not None:
#                         value = [h_start, intervals[i][-1]]
#                     else:
#                         value = [newInterval[0], intervals[i][-1]]
#                     result.append(value)
#                     result.extend(intervals[i+1:])
#                     return result
                
#                 elif newInterval[-1] > intervals[i][-1]:
#                     if h_start is not None:
#                         i += 1
#                     else:
#                         h_start = newInterval[0]
#                         i += 1

#             elif newInterval[0] > intervals[i][-1]:
#                 result.append(intervals[i])
#                 i += 1

#                 if i >= len(intervals):
#                     result.append(newInterval)
#                     return result

#     def is_in_interval(self, start: int, end: int, value: int) -> bool:
#         if start <= value <= end:
#             return True
#         return False


if __name__ == "__main__":
    print(Solution().insert([[1, 5]], [2,7]))