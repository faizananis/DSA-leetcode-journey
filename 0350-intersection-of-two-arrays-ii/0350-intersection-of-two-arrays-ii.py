class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        my_dict={}
        for n in nums1:
            if n in my_dict:
                my_dict[n]+=1
            else:
                my_dict[n]=1
        
        for i in nums2:
            if i in my_dict and my_dict[i]!=0:
                my_dict[i]-=1
                res.append(i)
        
        return res
        
