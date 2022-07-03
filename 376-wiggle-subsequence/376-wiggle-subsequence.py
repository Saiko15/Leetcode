class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        u,d = 0, 0
        last = None
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] and last != "up":
                last = "up"
                u += 1
            elif nums[i] < nums[i-1] and last != "down":
                last = "down"
                d += 1
        return u+d+1