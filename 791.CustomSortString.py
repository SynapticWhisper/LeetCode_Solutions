class Solution:
    def customSortString(self, order: str, s: str) -> str:
        values = {
            letter: index for index, letter in enumerate(order)
        }
        result = dict()
        not_ordered = []
        for l in s:
            index = values.get(l, None)
            if index is None:
                not_ordered.append(l)
            else:
                l_value = result.get(index, [])
                l_value.append(l)
                result[index] = l_value
        res = ""
        for i in range(len(order)):
            value = result.get(i, [])
            res += "".join(value)
        res += "".join(not_ordered)
        return res

if __name__ == "__main__":
    Solution().customSortString("cba", "abcd")