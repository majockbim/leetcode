class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        a1 = []
        a2 = []

        for i in nums1:
            if i not in nums2:
                a1.append(i)
                
        answer.append(list(set(a1)))
            
        for j in nums2:
            if j not in nums1:
                a2.append(j)

        answer.append(list(set(a2)))
        
        return answer