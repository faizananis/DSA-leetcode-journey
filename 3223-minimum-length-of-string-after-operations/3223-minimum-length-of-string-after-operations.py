class Solution:
    def minimumLength(self, s: str) -> int:
        my_hash=[0]*26
        result=0
        for char in s:
            my_hash[ord(char)-ord('a')]+=1
        for val in my_hash:
            if val==0:
                continue
            if val%2==0:
                result+=2
            elif val%2==1:
                result+=1
        return result