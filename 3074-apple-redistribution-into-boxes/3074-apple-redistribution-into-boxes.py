class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total=sum(apple)
        capacity.sort(reverse=True)
        count=0

        for i in range(len(capacity)):
            if total<=0:
                break
            total-=capacity[i]
            count+=1
        
        return count
