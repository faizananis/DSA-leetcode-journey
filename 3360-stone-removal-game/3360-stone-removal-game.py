class Solution:
    def canAliceWin(self, n: int) -> bool:
        val=10
        alice=False
        while n:
            if val>n:
                return alice
            else:
                n-=val
                alice = not alice
            val-=1
        return alice