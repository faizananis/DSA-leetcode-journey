class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=""
        for word in words:
            total=0
            for c in word:
                index=ord(c)-97
                total+=weights[index]
            print(total)
            ch=chr(122-total%26)
            ans+=ch
        return ans
