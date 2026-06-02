class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        t_i = 0
        n_i = 0
        t_len = len(typed)
        n_len = len(name)
        
        while t_i < t_len:
            if n_i < n_len and typed[t_i] == name[n_i]:
                n_i += 1
            elif t_i > 0 and typed[t_i] == typed[t_i - 1]:
                pass
            else:
                return False
            t_i += 1
        
        return n_i == n_len
