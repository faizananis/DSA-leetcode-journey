class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        my_dict={}
        result=0
        for word in words:  
            if word[::-1] in my_dict:
                my_dict[word[::-1]]-=1
                if my_dict[word[::-1]]==0:
                    del my_dict[word[::-1]]
                result+=4
            else:
                my_dict[word]=my_dict.get(word,0)+1
        print(my_dict)
        for [u,v] in my_dict:
            if u==v:
                result+=2
                break
        return result