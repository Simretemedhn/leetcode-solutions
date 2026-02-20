class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new = sorted(nums)

        total = 0
        order = [total]
        for i in range(1, len(nums)):
            if new[i] == new[i-1]:
                order.append(order[-1])
                total += 1
            else:
                total += 1
                order.append(total)

        output = []
        for i in range(len(nums)):
            output.append(order[new.index(nums[i])])

        return output 