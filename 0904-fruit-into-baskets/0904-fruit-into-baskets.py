class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        set_ = set()
        mapp = {}

        n = len(fruits)
        left = 0 
        longest = 0 
        for right in range(n):
            if fruits[right] in mapp:
                mapp[fruits[right]] += 1 
            else:
                mapp[fruits[right]] = 1 

            while len(mapp) > 2:
                #we have to shrink
                mapp[fruits[left]] -= 1 
                if mapp[fruits[left]] == 0:
                    del mapp[fruits[left]]
                left += 1  
            longest = max(longest, right - left + 1)
        return longest 
