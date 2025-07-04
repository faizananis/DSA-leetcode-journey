class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        word="a"
        for n in operations:
            if n==0:
                word+=word
            else:
                temp=""
                for w in word:
                    if w=='z':
                        temp+='a'
                    else:
                        temp+=chr(ord(w)+1)
                word+=temp
            if len(word)>k:
                break
        return word[k-1]