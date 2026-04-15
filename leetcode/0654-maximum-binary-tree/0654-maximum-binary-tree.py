# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def divide(arr):
            if not arr:  
                return None
            

            max_val = arr[0]
            max_idx = 0
            for i in range(1, len(arr)):
                if arr[i] > max_val:
                    max_val = arr[i]
                    max_idx = i
            

            left_arr = arr[:max_idx]
            right_arr = arr[max_idx + 1:]
            
            return max_val, left_arr, right_arr
        
        def conquer(arr):
            if not arr:
                return None
            
            root_val, left_arr, right_arr = divide(arr)
            
            root = TreeNode(root_val)
            
            root.left = conquer(left_arr)
            root.right = conquer(right_arr)
            
            return root
        
        return conquer(nums)


"""






            nodee.val = arr[0]
            nodee.left = find_max(left_arr)
            nodee.right = find_max(right_arr)

            return max_one[0]
"""          