class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        # Returns a 'dictionary' like {1: 3, 2: 2}
        counts = Counter(nums)
        # Returns a nested list of most common items, [[1,3],[2,2]]
        m = counts.most_common(k)

        # add most common digits
        r = []
        for item in m:
            r.append(item[0])

        return r