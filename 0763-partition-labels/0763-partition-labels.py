class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        my_dict={}
        result=[]
        for i in range(len(s)):
            my_dict[s[i]]=i
        i=0
        while i<len(s):
            end=my_dict[s[i]]
            j=i
            while j<end:
                end=max(end,my_dict[s[j]])
                j+=1
            result.append(j-i+1)
            i=j+1
        return result