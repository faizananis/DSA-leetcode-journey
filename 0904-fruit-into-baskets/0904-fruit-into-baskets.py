class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        my_dict={}
        max_size=0
        for right in range(len(fruits)):
            if fruits[right] not in my_dict:
                my_dict[fruits[right]]=1
            else:
                my_dict[fruits[right]]+=1
            while len(my_dict)>2 and left<right:
                my_dict[fruits[left]]-=1
                if my_dict[fruits[left]]==0:
                    del my_dict[fruits[left]]
                left+=1
            max_size=max(max_size,right-left+1)
        return max_size