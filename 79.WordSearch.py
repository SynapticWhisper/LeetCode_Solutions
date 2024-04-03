from functools import reduce
from collections import Counter

class Solution:
    ACTIONS: list = [ 
        lambda row, col: (row-1, col),
        lambda row, col: (row+1, col),
        lambda row, col: (row, col-1),
        lambda row, col: (row, col+1)
    ]

    def exist(self, board: list[list[str]], word: str) -> bool:

        self.maxValues: tuple = len(board), len(board[0])
        self.board = board
        self.word = word
        self.visited: set = set()

        if len(word) > self.maxValues[0]*self.maxValues[-1]:
            return False
        
        count = Counter(sum(board, []))
        
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False


        for row in range(self.maxValues[0]):
            for col in range(self.maxValues[-1]):
                if self.find_ways(0, (row, col)):
                    return True
        return False
        
    def find_ways(self, i: int, start: tuple) -> bool:
        mR, mC = self.maxValues
        r, c = start

        if i == len(self.word):
            return True
        
        if r < 0 or c < 0 or r >= mR or c >= mC or start in self.visited:
            return False

        if self.board[r][c] != self.word[i]:
            return False

        self.visited.add(start)
        res: bool = reduce(
            lambda x, y: x | y,
            [self.find_ways(i+1, action(*start)) for action in self.ACTIONS]
        )
        self.visited.remove(start)

        return res


if __name__ == "__main__":
    Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")