from collections import Counter
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        ST = Counter(students)

        for item in sandwiches:
            count = ST.get(item, 0)
            if count <= 0:
                break
            count -= 1
            ST[item] = count
        else:
            return 0
        return sum([item for item in ST.values()])
            

if __name__ == "__main__":
    print(Solution().countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))