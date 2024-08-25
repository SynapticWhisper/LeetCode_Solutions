from test import test

class Solution:
    def reverseParentheses(self, s: str) -> str:
        queue = []
        tmp = ''

        for simbol in s:
            if simbol in ('(', ')'):
                if simbol == "(":
                    queue.insert(0, tmp)
                    tmp = ''
                elif simbol == ")":
                    if queue:
                        tmp = queue.pop(0) + tmp[::-1]
                    else:
                        tmp = tmp[::-1]
            else:
                tmp += simbol

        return tmp


if __name__ == "__main__":
    test_cases = {
        "Test 1": {
            "args": ("(abcd)",),
            "kwargs": {},
            "answer": "dcba"
        },
        "Test 2": {
            "args": ("(u(love)i)",),
            "kwargs": {},
            "answer": "iloveu"
        },
        "Test 3": {
            "args": ("(ed(et(oc))el)",),
            "kwargs": {},
            "answer": "leetcode"
        }
    }
    test(Solution().reverseParentheses, test_cases)