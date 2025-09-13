class Solution:
    def maxFreqSum(self, s: str) -> int:
        maxVowel=0
        maxCons=0
        my_dict={}
        my_set={'a','e','i','o','u'}
        for c in s:
            if c in my_dict:
                my_dict[c]+=1
            else:
                my_dict[c]=1

            if c in my_set:
                maxVowel=max(maxVowel,my_dict[c])
            else:
                maxCons=max(maxCons,my_dict[c])
        return maxVowel+maxCons