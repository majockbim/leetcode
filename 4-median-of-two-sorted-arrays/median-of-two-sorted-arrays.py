class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:\

        length = len(nums1) + len(nums2)

        for num in nums2:
            nums1.append(num)
        
        nums1.sort()
        
        if length % 2 != 0:
            med = length // 2
            return nums1[med]
        else:
            median = (length // 2) - 1
            med = (nums1[median] + nums1[median + 1]) / 2
            return float(med)