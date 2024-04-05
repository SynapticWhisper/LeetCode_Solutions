class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s):
            if i + 1 >= len(s):
                return s
            
            if s[i].swapcase() == s[i+1]:
                s = s[:i] + s[i+2:]
                i = max(i-1, 0)
            
            else:
                i += 1
        return s