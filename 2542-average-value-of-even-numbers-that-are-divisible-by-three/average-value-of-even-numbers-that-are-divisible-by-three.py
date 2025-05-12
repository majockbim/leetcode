class Solution:
    def averageValue(self, nums: List[int]) -> int:

        avg = 0
        count = 0
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                count += 1
                avg += num
        
        if count != 0:
            return int(avg / count)
        else:
            return 0
