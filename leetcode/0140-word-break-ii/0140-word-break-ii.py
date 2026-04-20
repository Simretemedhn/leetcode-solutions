class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        result = []
        
        def dfs(start, current_sentence):
            if start == len(s):
                result.append(' '.join(current_sentence))
                return
            
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    current_sentence.append(word)
                    dfs(end, current_sentence)
                    current_sentence.pop()
        
        dfs(0, [])
        return result


"""class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:


        wordDict = set(wordDict)
        n = len(s)
        sentence = []
        collection = []
        def check(starting_ind):
            if starting_ind == n and sentence[-1][-1] == s[-1]:
                return True 
            elif starting_ind == n and sentence[-1][-1] != s[-1]:
                return False 
            for i in range(starting_ind+1, n):
                if s[starting_ind:i] in wordDict:
                    sentence.append(s[starting_ind:i])
                    check(i+1)


        collection = []
        for i in range(1, n):
            if check(i):
                collection.extend(sentence)
            else:
                sentence = []


        check(0)
        return collection
"""