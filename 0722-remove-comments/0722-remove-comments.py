class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        in_block = False
        current = []
        
        for line in source:
            i = 0
            while i < len(line):
                two_chars = line[i:i+2]
                
                if not in_block:
                    if two_chars == '/*':
                        in_block = True
                        i += 1
                    elif two_chars == '//':
                        break
                    else:
                        current.append(line[i])
                else:
                    if two_chars == '*/':
                        in_block = False
                        i += 1
                
                i += 1
            
            if current and not in_block:
                result.append(''.join(current))
                current = []
        
        return result