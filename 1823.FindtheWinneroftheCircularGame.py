class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends_numbers = [i for i in range(1, n+1)]
        start_position = 0
        
        def get_loser(counter: int, start_position: int) -> int:
            if counter > len(friends_numbers):
                return get_loser(counter - len(friends_numbers), start_position)
            else:
                loser_index = start_position + (counter - 1)
                if loser_index > len(friends_numbers) - 1:
                    loser_index -= len(friends_numbers)
                return loser_index

        while len(friends_numbers) > 1:
            loser_position = get_loser(k, start_position)
            friends_numbers.pop(loser_position)
            start_position = loser_position if loser_position <= len(friends_numbers) - 1 else 0
        return friends_numbers[0]