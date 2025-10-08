class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans=[]
        potions.sort()
        for n in spells:
            left=0
            right=len(potions)-1
            if n*potions[right]<success:
                ans.append(0)
                continue
            while left<right:
                mid=(left+right)//2
                if n*potions[mid]>=success:
                    right=mid
                else:
                    left=mid+1
            ans.append(len(potions)-right)
        return ans