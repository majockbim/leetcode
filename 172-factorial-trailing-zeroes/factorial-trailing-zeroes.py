class Solution:
    def trailingZeroes(self, n: int) -> int:
        import sys
        import math


        sys.set_int_max_str_digits(0)
        nf = str(math.factorial(n))
        nr = nf[::-1]

        count = 0
        for i in nr:
            if int(i) == 0:
                count += 1
            else:
                return count
