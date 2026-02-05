class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """common_elems = []
        common_ind = []
        for elem in list1:
            if elem in list2: 
                common_elems.append(elem)
                common_ind.append(list1.index(elem)+ list2.index(elem))
        ind = min(common_ind)
        find = common_ind.index(ind)
        return [common_elems[find]]"""



class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {name: i for i, name in enumerate(list2)}
        min_sum = float('inf')
        result = []

        for i, name in enumerate(list1):
            if name in index_map:
                curr_sum = i + index_map[name]

                if curr_sum < min_sum:
                    min_sum = curr_sum
                    result = [name]
                elif curr_sum == min_sum:
                    result.append(name)

        return result

