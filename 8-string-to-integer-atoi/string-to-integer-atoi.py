class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        mag = ""
        sign = 1
        i = 0

        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i +=1

        while i < len(s) and s[i].isdigit():
            mag += s[i]
            i += 1

        if not mag:
            return 0

        res = int(mag) * sign

        if res > 2**31 - 1:
            return 2**31 - 1
        elif res < -2**31:
            return -2**31
        return res