from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        row_l = len(points)
        col_l = len(points[0])

        for i in range(1, row_l):
            for j in range(col_l):
                value = points[i][j]
                points[i][j] = max([
                    value + points[i-1][x] - abs(j-x) for x in range(col_l)
                ])
        return max(points[-1])