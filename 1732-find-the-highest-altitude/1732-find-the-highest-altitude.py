class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=0
        val=0
        for n in gain:
            val+=n
            ans=max(ans,val)
        return ans