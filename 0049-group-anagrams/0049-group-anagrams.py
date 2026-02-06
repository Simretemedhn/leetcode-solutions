class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicc = {}
        for strss in strs:
            anag = "".join(sorted(strss))
       
            if anag not in dicc:
                dicc[anag] = []
            dicc[anag].append(strss)
        return list(dicc.values()) 



            



            

        