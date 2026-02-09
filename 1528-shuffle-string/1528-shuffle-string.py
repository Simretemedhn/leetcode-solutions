class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        indice_map = {}

        for x in range(len(s)):
            indice_map[x] = s[indices.index(x)]
        list1 = [letter for letter in  indice_map.values()]
        return "".join(list1)

        """list2 = []
        for x in range(len(s)):
            list2.append(s[indices.index(x)])
        return "".join(list2) """