from collections import Counter 

class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        value = tickets[k]

        if value == 1:
            return k + 1
        
        values = Counter(tickets)

        counter = 0
        values_count = len(tickets)

        for i in range(0, value-1):
            values_count -= values[i]
            counter += values_count

        for i in range(k):
            if tickets[i] >= value:
                counter += 1
        counter += 1

        return counter

    
if __name__ == "__main__":
    print(Solution().timeRequiredToBuy([5, 1, 1, 1], 0))