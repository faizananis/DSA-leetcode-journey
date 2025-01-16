class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans=0
        if len(nums1)&1==0 and len(nums2)&1==0:
            return 0  
        if len(nums1)&1==0:
            for n in nums1:
                ans^=n
        elif len(nums2)&1==0:
            for n in nums2:
                ans^=n
        else:
            for n in nums1:
                ans^=n
            for n in nums2:
                ans^=n
        return ans