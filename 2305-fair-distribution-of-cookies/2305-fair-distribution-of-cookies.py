class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribution = [0] * k
        self.best = float('inf')
        
        cookies.sort(reverse=True)
        
        def backtrack(index):
            if max(distribution) >= self.best:
                return
            
            if index == len(cookies):
                self.best = min(self.best, max(distribution))
                return
            
            for child in range(k):
                if child > 0 and distribution[child] == distribution[child - 1]:
                    continue
                
                distribution[child] += cookies[index]
                backtrack(index + 1)
                distribution[child] -= cookies[index]
                
                if distribution[child] == 0:
                    break
        
        backtrack(0)
        return self.best