class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        for i in range(k):
            happiness[i]-=i
            if happiness[i]<0:
                happiness[i]=0
            
        return sum(happiness[:k])