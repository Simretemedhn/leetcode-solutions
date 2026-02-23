class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right, chemistry = 0, len(skill)-1, 0
        n = len(skill)//2
        result = sum(skill)/n
        if len(skill) % 2 !=0:
            return -1
        for x in range(n):
            if skill[left] + skill[right] == result:
                chemistry += skill[left]*skill[right]
                left += 1
                right -= 1
            else:
                return -1
            
            
        return chemistry