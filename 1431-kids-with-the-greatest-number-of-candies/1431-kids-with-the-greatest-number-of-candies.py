class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer=[]
        maxCandies=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies < maxCandies:
                answer.append(False)
            else:
                answer.append(True)
        return answer