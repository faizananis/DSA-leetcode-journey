class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count = bin(num2).count('1')
        res = 0

        # Cancel set bits from highest to lowest weight
        for i in range(31, -1, -1):
            if (num1 & (1 << i)):
                count -= 1
                res += (1 << i)
            if count == 0:
                break

        # Set bits lowest to highest weight
        for i in range(32):
            if (num1 & (1 << i)) == 0:
                count -= 1
                res += (1 << i)
            if count == 0:
                break

        return res