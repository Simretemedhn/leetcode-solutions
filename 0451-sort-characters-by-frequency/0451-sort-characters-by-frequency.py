class Solution:
    def frequencySort(self, s: str) -> str:
        
        
        letter_map = {}
        for char in s:
            letter_map[char] = letter_map.get(char, 0) + 1

        output = []
        sorted_dict = dict(sorted(letter_map.items(), key=lambda x: x[1], reverse=True))
        for each, freq in sorted_dict.items():
            output.append(each*freq)
        return "".join(output)
