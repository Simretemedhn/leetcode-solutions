from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        collect = SortedList()

        def divide(arr, num):
            less_count = arr.bisect_left(num)
            great_count = len(arr) - arr.bisect_right(num)
            arr.add(num)
            
            return less_count, great_count

        cost = 0
        MOD = 10**9 + 7
        
        for i in range(len(instructions)):
            less_, greater_ = divide(collect, instructions[i])
            cost += min(less_, greater_)

        return cost % MOD
                    
                