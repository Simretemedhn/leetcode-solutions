class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1,n+1))
        ind = 0 

        while len(friends) > 1:
            ind = (ind + k - 1 ) % len(friends)
            friends.pop(ind)

        return friends[0] 
