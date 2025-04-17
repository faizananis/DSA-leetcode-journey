class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict={}
        maxSize=0
        left=0
        for right in range(len(s)):
            if s[right] in my_dict:
                my_dict[s[right]]+=1
            else:
                my_dict[s[right]]=1
            size=right-left+1
            while len(my_dict)<size:
                my_dict[s[left]]-=1
                if my_dict[s[left]]==0:
                    del my_dict[s[left]]
                left+=1
                size-=1
            maxSize=max(maxSize,size)
        return maxSize



            