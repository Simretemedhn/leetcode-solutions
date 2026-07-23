from collections import Counter 
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = [match[0] for match in matches]
        loser = [match[1] for match in matches]

        all_time_winner = list(set(winner) - set(loser))
        one_time_loser = [num for num, freq in Counter(loser).items() if freq == 1]
        all_time_winner.sort()
        one_time_loser.sort()

        return [all_time_winner, one_time_loser]