class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        my_dict={}
        p1=0
        p2=0
        while p1<len(nums1) or p2<len(nums2):
            if p1<len(nums1):
                if nums1[p1][0] not in my_dict:
                    my_dict[nums1[p1][0]]=nums1[p1][1]
                else:
                    my_dict[nums1[p1][0]]+=nums1[p1][1]
                p1+=1
            if p2<len(nums2):
                if nums2[p2][0] not in my_dict:
                    my_dict[nums2[p2][0]]=nums2[p2][1]
                else:
                    my_dict[nums2[p2][0]]+=nums2[p2][1]
                p2+=1
        ans=sorted(list(my_dict.items()))
        return ans