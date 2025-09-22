class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        my_dict={}
        maximum=0
        for i in range(len(nums)):
            if nums[i] in my_dict:
                my_dict[nums[i]]+=1
            else:
                my_dict[nums[i]]=1
            maximum=max(maximum,my_dict[nums[i]])
        count=0
        my_list=my_dict.values()
        for n in my_list:
            if n==maximum:
                count+=1
        return count*maximum