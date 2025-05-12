class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:\

        length = len(nums1) + len(nums2)

        # Combine the arrays
        for num in nums2:
            nums1.append(num)
        
        # Sort the integers in array (ascending order)
        nums1.sort()
        
        # If odd number of elements, return middle number
        if length % 2 != 0:
            med = length // 2
            return nums1[med]

        # If even number of elements, return mean of middle numbers
        else:
            median = (length // 2) - 1 # 0-based indexing
            med = (nums1[median] + nums1[median + 1]) / 2
            return med