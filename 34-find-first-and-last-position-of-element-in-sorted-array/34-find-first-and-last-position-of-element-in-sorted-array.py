class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_target_index = self.binary_search_on_left(nums, target, 0, len(nums) - 1)
        if left_target_index == -1:
            return [-1, -1]
        
        right_target_index = self.binary_search_on_right(nums, target, 0, len(nums) - 1)
        return [left_target_index, right_target_index]
    
    def binary_search_on_left(self, nums: list[int], target: int, left: int, right: int):
        index_on_left = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                index_on_left = mid
            
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
            
        return index_on_left
            
    
    def binary_search_on_right(self, nums: list[int], target: int, left: int, right: int):
        index_on_right = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                index_on_right = mid
            
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
            
        return index_on_right