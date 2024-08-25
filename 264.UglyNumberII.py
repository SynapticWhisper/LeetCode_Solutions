class Solution:
    def nthUglyNumber(self, n: int) -> int:
        result: list = []
        result.append(1)
        count_2, count_3, count_5 = 0, 0, 0
        for i in range(1, n+1):
            value_2 = result[count_2]*2
            value_3 = result[count_3]*3
            value_5 = result[count_5]*5

            tmp = min(value_2, value_3, value_5)

            if tmp == value_2:
                count_2 += 1
            if tmp == value_3:
                count_3 += 1
            if tmp == value_5:
                count_5 += 1
            result.append(tmp)
        return result[n-1]