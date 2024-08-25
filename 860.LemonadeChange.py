from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5 = 0
        count_10 = 0
        for bill in bills:

            if bill == 5:
                count_5 += 1
            elif bill == 10:
                count_10 += 1
                count_5 -= 1
            else:
                if count_10 < 1:
                    count_5 -= 3
                else:
                    count_10 -= 1
                    count_5 -= 1

            if count_5 < 0:
                return False
        return True



if __name__ == "__main__":
    Solution().lemonadeChange([5,5,5,10,20])