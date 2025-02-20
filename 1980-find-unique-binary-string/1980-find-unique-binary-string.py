class Solution:
    def __init__(self):
        self.res = ""

    def buildNumber(self, numbers, curr, n):
        if len(curr) == n:
            if curr not in numbers:
                self.res = curr
                return True
            return False

        # Try '0'
        if self.buildNumber(numbers, curr + '0', n):
            return True

        # Try '1'
        if self.buildNumber(numbers, curr + '1', n):
            return True

        return False

    def findDifferentBinaryString(self, nums: List[str]) -> str::
        n = len(nums)
        numbers = set(nums)
        self.buildNumber(numbers, "", n)
        return self.res
        