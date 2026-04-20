
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)  
        n = len(s)
        collection = []

        def backtracking(start, current_sentence):
            if start == n:
                collection.append(' '.join(current_sentence))
                return
            
            for end in range(start + 1, n + 1): 
                word = s[start:end]
                if word in wordSet:
                    current_sentence.append(word)
                    backtracking(end, current_sentence)  
                    current_sentence.pop()
        
        backtracking(0, [])
        return collection