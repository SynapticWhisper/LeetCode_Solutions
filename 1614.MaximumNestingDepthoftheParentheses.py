class Solution:
    def maxDepth(self, s: str) -> int:
        sub_max: int = 0
        opened: int = 0
        
        for letter in s:
            if letter == "(":
                opened += 1
            elif letter == ")":
                sub_max = max(opened, sub_max)
                opened -= 1
        return sub_max
                    
if __name__ == "__main__":
    print(Solution().maxDepth("(1)+((2))+(((3)))"))