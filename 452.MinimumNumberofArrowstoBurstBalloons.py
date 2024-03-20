class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()

        i = 0

        while i < len(points) and i+1 < len(points):
            value = points[i]
            
            next_value = points[i+1]

            if value[-1] < next_value[0]:
                arrow_counter += 1
                i += 1
            elif value[-1] == next_value[0]:
                points.pop(i+1)
                points[i] = [value[-1], value[-1]]
            elif value[-1] > next_value[0]:
                points.pop(i+1)
                points[i] = [next_value[0], min(value[-1], next_value[-1])]

        return len(points)
    
if __name__ == "__main__":
    print(Solution().findMinArrowShots([[4,12],[7,8],[7,9],[7,9],[2,8],[6,7],[5,14],[4,13]]))