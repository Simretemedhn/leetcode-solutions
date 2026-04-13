class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if 3 * pow(2, n - 1) < k:
            return ""
        count = 0
        letters = ["a", "b", "c"]
        final = None 
        
        def helper(subseq):
            nonlocal count, final  
            
            if len(subseq) == n:  
                count += 1 
                if count == k:
                    final = "".join(subseq)  
                return 
            
            for letter in letters:
                if not subseq or subseq[-1] != letter:
                    subseq.append(letter)
                    helper(subseq)
                    subseq.pop() 
                    if final: 
                        return
        
        helper([])
        return final if final else ""