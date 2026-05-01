from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        
        def get_coordinates(square):
            square -= 1
            row = n - 1 - (square // n)
            col = square % n
            if (n - 1 - row) % 2 == 1:
                col = n - 1 - col
            return row, col
        
        visited = set()
        queue = deque()
        queue.append((1, 0))
        visited.add(1)
        
        while queue:
            curr, moves = queue.popleft()
            
            for dice in range(1, 7):
                next_square = curr + dice
                
                if next_square > target:
                    continue
                
                row, col = get_coordinates(next_square)
                if board[row][col] != -1:
                    next_square = board[row][col]
                
                if next_square == target:
                    return moves + 1
                
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        
        return -1