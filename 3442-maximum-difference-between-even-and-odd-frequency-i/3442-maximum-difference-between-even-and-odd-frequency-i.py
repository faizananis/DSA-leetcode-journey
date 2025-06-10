class Solution:
    def maxDifference(self, s: str) -> int:
        freq=Counter(s)
        maximum=0
        minimum=float("inf")
        for val in freq:
            if freq[val]&1:
                maximum=max(maximum,freq[val])
            else:
                minimum=min(minimum,freq[val])
        return maximum-minimum