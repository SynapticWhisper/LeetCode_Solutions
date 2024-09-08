from string import ascii_lowercase
from functools import reduce

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabet = {
            letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)
        }

        pre_result = ""
        for i in s:
            pre_result += alphabet.get(i)
        
        while k > 0:
            result = reduce(lambda x, y: int(x) + int(y), pre_result)
            pre_result = str(result)
            k -= 1
        
        return int(result)

if __name__ == "__main__":
    Solution().getLucky("dbvmfhnttvr", 5)
