class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied=0
        slide=0
        maxSlide=0
        n=len(customers)
        for i in range(n):
            if grumpy[i]==0:
                satisfied+=customers[i]
        for i in range(n):
            if grumpy[i]==1:
                slide+=customers[i]
            if i>=minutes:
                if grumpy[i-minutes]==1:
                    slide-=customers[i-minutes]
            maxSlide=max(maxSlide,slide)
        return satisfied+maxSlide