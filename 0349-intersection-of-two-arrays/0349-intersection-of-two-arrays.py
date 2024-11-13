class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        s=set()
        for n in nums1:
            s.add(n)
        
        for n in nums2:
            if n in s:
                result.append(n)
                s.remove(n)
        
        return result