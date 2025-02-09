class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        my_dict={}
        good_pairs=0
        n=len(nums)
        for i in range(n):
            if i-nums[i] in my_dict:
                good_pairs+=my_dict[i-nums[i]]
                my_dict[i-nums[i]]+=1
            else:
                my_dict[i-nums[i]]=1
        total_pairs=n*(n-1)//2
        return total_pairs-good_pairs