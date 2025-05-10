class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        total_sum1=sum(nums1)+nums1.count(0)
        total_sum2=sum(nums2)+nums2.count(0)
        if total_sum1==total_sum2:
            return total_sum1
        if total_sum1<total_sum2:
            if nums1.count(0)==0:
                return -1
            return total_sum2
        if total_sum2<total_sum1:
            if nums2.count(0)==0:
                return -1
            return total_sum1
        
