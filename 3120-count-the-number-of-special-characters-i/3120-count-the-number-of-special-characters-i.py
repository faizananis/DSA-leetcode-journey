class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        my_set=set(word)
        count=0
        for c in range(65,91):
            if chr(c) in my_set and chr(c+32) in my_set:
                count+=1
        return count