class Solution:
    def doesAliceWin(self, s: str) -> bool:
        my_set={'a','e','i','o','u'}
        count=0
        for c in s:
            if c in my_set:
                return True
        return False