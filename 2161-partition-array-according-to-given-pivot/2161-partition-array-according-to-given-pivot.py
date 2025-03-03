class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                result.append(nums[i])
        for j in range(len(nums)):
            if nums[j]==pivot:
                result.append(nums[j])
        for k in range(len(nums)):
            if nums[k]>pivot:
                result.append(nums[k])
        return result


        # small=0
        # temp=0
        # for i in range(len(nums)):
        #     if nums[i]<pivot:
        #         temp=nums[i]
        #         nums[i]=nums[small]
        #         nums[small]=temp
        #         small+=1
        # equal=small
        # if equal<len(nums):
        #     for i in range(equal,len(nums)):
        #         if nums[i]==pivot:
        #             temp=nums[i]
        #             nums[i]=nums[equal]
        #             nums[equal]=temp
        #             equal+=1
        # large=equal
        # if large<len(nums):
        #     for i in range(large,len(nums)):
        #         if nums[i]>pivot:
        #             temp=nums[i]
        #             nums[i]=nums[large]
        #             nums[large]=temp
        #             large+=1
        # return nums
            

        # n = len(nums)
        # res = [0] * n
        
        # left, right = 0, n - 1
        # left_res, right_res = 0, n - 1
        
        # while left < n:
        #     if nums[left] < pivot:
        #         res[left_res] = nums[left]
        #         left_res += 1
        #     if nums[right] > pivot:
        #         res[right_res] = nums[right]
        #         right_res -= 1
        #     left += 1
        #     right -= 1
        
        # while left_res <= right_res:
        #     res[left_res] = pivot
        #     left_res += 1
        
        # return res