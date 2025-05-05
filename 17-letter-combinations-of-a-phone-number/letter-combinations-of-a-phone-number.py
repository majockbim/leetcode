class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 2d list for easy access
        keyboard = [
           ["a", "b", "c"],
           ["d", "e", "f"],
           ["g", "h", "i"],
           ["j", "k", "l"],
           ["m", "n", "o"],
           ["p", "q", "r", "s"],
           ["t", "u", "v"],
           ["w", "x", "y", "z"]
        ]

        if len(digits) == 1:
           return keyboard[int(digits) - 2]

        # separate digits into a list
        digits = [int(b) for b in str(digits) if b in "23456789"]
        if not digits:
            return []

        result = keyboard[digits[0] - 2]

        for i in range(1, len(digits)):
            temp = []
            for prefix in result:
                for char in keyboard[digits[i] - 2]:
                    temp.append(prefix + char)
            result = temp
      
        return result