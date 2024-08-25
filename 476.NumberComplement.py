class Solution:
    def findComplement(self, num: int) -> int:
        stop = (1 << num.bit_length()) - 1
        
        return stop ^ num
    
print(Solution().findComplement(5))