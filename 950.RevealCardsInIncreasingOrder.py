class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort()
        l = len(deck)
        if l <= 2:
            return deck
        cache = [deck[-1]]
        for i in range(l-2, -1, -1):
            cache = [deck[i], cache[-1]] + cache[:-1]
        return cache 


if __name__ == "__main__":
    Solution().deckRevealedIncreasing([17,13,11,2,3,5,7])