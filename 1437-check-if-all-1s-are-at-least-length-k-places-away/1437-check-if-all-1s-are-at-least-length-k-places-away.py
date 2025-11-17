class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dist=-1
        for i in range(len(nums)):
            if nums[i]==1:
                if dist==-1:
                    dist=i
                elif i-dist-1<k:
                    return False
                else:
                    dist=i
        return True
