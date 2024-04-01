class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    
if __name__ == "__main__":
    Solution().lengthOfLastWord(s="Hello World")