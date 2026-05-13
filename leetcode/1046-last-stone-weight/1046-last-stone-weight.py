class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        while len(stones) > 1:
            max_first = max(stones)
            stones.remove(max_first)
            max_second =  max(stones)
            stones.remove(max_second)

            if max_first != max_second:
                stones.append(abs(max_first - max_second))
        return stones[0] if len(stones) == 1 else 0