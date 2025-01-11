class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k>len(s):
            return False
        my_arr=[0]*26
        for c in s:
            my_arr[ord(c)-ord('a')]+=1
        count_odd_freq=0
        for val in my_arr:
            if val%2==1:
                count_odd_freq+=1
        if count_odd_freq<=k:
            return True
        return False
        