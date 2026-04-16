class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans=float("inf")
        if words[startIndex]==target:
            return 0
        n=len(words)
        i=(startIndex+1)%n
        j=1
        while i!=startIndex:
            if words[i]==target:
                break
            i=(i+1)%n
            j+=1
        if i==startIndex:
            return -1
        ans=j
        i=(startIndex-1)%n
        j=1
        while i!=startIndex:
            if words[i]==target:
                break
            i=(i-1)%n
            j+=1
        ans=min(ans,j)
        return ans