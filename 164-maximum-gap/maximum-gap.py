class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        nums.sort()

        element = len(nums) - 1
        count = 0
        while element >= 1:
            if count < (nums[element] - nums[element - 1]):
                count = (nums[element] - nums[element - 1])
            
            element -= 1
        
        return count