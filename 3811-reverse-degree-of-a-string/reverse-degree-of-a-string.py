class Solution:
    def reverseDegree(self, s: str) -> int:

        ans = 0
        n = len(s)
        for i in range(len(s)):
            r_v = 26 - (ord(s[i]) - ord('a'))
            ans += r_v * (i + 1)

        return ans


        