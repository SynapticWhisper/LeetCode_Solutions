class Solution:
    def pivotInteger(self, n: int) -> int:
        values = list(range(1, n+1))
        
        for i in range(len(values)-2, 0, -1):
            if sum(values[:i+1]) == sum(values[i:]):
                return values[i]
        return -1

if __name__ == "__main__":
    Solution().pivotInteger(8)