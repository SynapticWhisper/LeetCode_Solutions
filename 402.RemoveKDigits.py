class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        
        if k == 1:
            for i in range(len(num)):
                if i == len(num) - 1:
                    return num[:-1]
                if num[i] > num[i+1]:
                    num = list(num[:i] + num[i+1:])
                    while num and num[0] == "0":
                        num.pop(0)
                    return "".join(num) if num else "0"
                    
        if k >= len(num.replace("0", "")):
            return "0"
        
        num = list(num)

        index = 0
        while k > 0:
            if index >= len(num):
                for _ in range(k):
                    num.pop()
                break
            if index - 1 > -1 and num[index] < num[index - 1]:
                num.pop(index-1)
                k -= 1
                index -= 1
            elif index + 1 < len(num) and num[index] > num[index + 1]:
                num.pop(index)
                k -= 1
            else:
                index += 1

        while num[0] == "0":
            num.pop(0)
        return "".join(num)
        
        # Run time error
        
        # K = k
        # result = []
        # start = 0
        # while k > 0 and len(result) < len(num) - K:
        #     item_index = None
        #     sub_min = 10
        #     for i, n in enumerate(num[start:start+k+1]):
        #         if int(n) < sub_min:
        #             sub_min = int(n)
        #             item_index = start + i
        #     result.append(sub_min)
        #     k -= (item_index - start)
        #     start = item_index + 1
        # if len(result) < len(num) - K:
        #     result.extend(map(lambda x: int(x), num[start:]))
        # return str(int("".join(map(lambda x: str(x), result))))

if __name__ == "__main__":
    print(Solution().removeKdigits("9999999999991", k=8))

        