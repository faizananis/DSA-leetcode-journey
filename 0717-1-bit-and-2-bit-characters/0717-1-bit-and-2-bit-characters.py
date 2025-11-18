class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits)==1:
            return True
        return bits[-1]==bits[-2] and bits[-1]==0