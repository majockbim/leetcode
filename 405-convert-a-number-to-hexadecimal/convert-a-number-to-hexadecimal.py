class Solution:
    def toHex(self, num: int) -> str:

        if num >= 0:
            return hex(num)[2:]
        else:
            # Convert number to binary
            bin_num = bin(abs(num))[2:].zfill(32)

            # Swaps 0's with 1's, and vice versa
            invert = ''.join('1' if b == '0' else '0' for b in bin_num)

            # Convert to integer, add one, back to binary
            tc_int = int(invert, 2) + 1
            tc_bin = bin(tc_int)[2:].zfill(32)

            # Convert to hex
            hex_num = hex(int(tc_bin, 2))[2:]

            return hex_num

 

        