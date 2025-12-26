class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binary1=a
        binary2=b

        decimal_sum=int(binary1,2) + int(binary2,2)
        binary_result=bin(decimal_sum)
        return binary_result[2:]