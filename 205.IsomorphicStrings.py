class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cache_1: dict = {}
        cache_2: dict = {}
        for i in range(len(s)):
            l_1, l_2 = s[i], t[i]
            target_1 = cache_1.get(l_1, None)
            target_2 = cache_2.get(l_2, None)
            if target_1 is None and target_2 is None:
                cache_1[l_1], cache_2[l_2] = l_2, l_1
            else:
                if target_1 != l_2 or target_2 != l_1:
                    return False

        return True
    
if __name__ == "__main__":
    Solution().isIsomorphic(s="egg", t="add")