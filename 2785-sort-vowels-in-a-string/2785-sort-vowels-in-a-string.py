class Solution:
    def sortVowels(self, s: str) -> str:
        my_list=[]
        my_set={'A','E','I','O','U','a','e','i','o','u'}
        for c in s:
            if c in my_set:
                my_list.append(c)
        my_list.sort()
        j=0
        s=list(s)
        for i in range(len(s)):
            if s[i] in my_set:
                s[i]=my_list[j]
                j+=1
        return "".join(s)