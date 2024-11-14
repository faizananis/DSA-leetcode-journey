class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # result=[]
        # s=set()
        # for n in nums1:
        #     s.add(n)
        
        # for n in nums2:
        #     if n in s:
        #         result.append(n)
        #         s.remove(n)
        
        # return result

        result=[]
        my_dict={}
        for n in nums1:
            if n in my_dict:
                my_dict[n]+=1
            else:
                my_dict[n]=1
        
        for i in nums2:
            if i in my_dict and my_dict[i]!=0 and i not in result:
                my_dict[i]-=1
                result.append(i)
        
        return result