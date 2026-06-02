class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        front = 0 
        back = len(s)-1 
        letters = list(s)
        while front < back:
            if not letters[front].isalpha():
                front += 1 
            elif not letters[back].isalpha():
                back -= 1 
            else:
                letters[front], letters[back] = letters[back], letters[front]
                front += 1 
                back -= 1 
        return "".join(letters)
        