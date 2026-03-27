class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        hash_map={}
        my_set=set(nums)
        for i in my_set:
            n=i
            count=0
            while n:
               count+=n&1
               n//=2
            if count not in hash_map:
                hash_map[count]=1
            else:
                hash_map[count]+=1

        result=0

        for i in hash_map:
            for j in hash_map:
                if i+j>=k:
                    result+=hash_map[i]*hash_map[j]
        
        return result
