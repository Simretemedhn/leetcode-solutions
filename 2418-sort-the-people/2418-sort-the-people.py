class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(n-1):
            for x in range(i+1, n):
                if heights[i] < heights[x]:
                    heights[i], heights[x] = heights[x], heights[i]
                    names[i], names[x] = names[x], names[i]
        return names
        