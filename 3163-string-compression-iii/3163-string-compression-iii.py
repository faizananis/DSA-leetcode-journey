class Solution:
    def compressedString(self, word: str) -> str:
        comp=""
        count=0
        prev=word[0]
        for i in range(len(word)):
            if prev==word[i] and count<9:
                count+=1
            else:
                comp+=str(count)+prev
                count=1
            prev=word[i]
        comp+=str(count)+prev
        return comp