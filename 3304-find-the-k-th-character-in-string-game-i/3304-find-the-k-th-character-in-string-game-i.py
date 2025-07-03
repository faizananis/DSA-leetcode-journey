class Solution:
    def kthCharacter(self, k: int) -> str:
        word="a"
        while len(word)<k:
            next=""
            for w in word:
                if w=='z':
                    next+='a'
                else:
                    next+=chr(ord(w)+1)
            word+=next
        return word[k-1]
