class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        a = 0
        b = 1
        c = 1

        counter = 2

        while counter < n:
            t = a + b + c
            a, b, c = b, c, t
            counter += 1
        return c

if __name__ == "__main__":
    print(Solution().tribonacci(4))