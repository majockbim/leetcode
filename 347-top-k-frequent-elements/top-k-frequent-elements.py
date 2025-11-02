class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        counts = Counter(nums)
        m = counts.most_common(k)

        r = []
        for item in m:
            r.append(item[0])

        return r