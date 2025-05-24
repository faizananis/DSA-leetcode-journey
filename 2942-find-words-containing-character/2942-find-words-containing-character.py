class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result=[]
        for i in range(len(words)):
            for j in words[i]:
                if j==x[0]:
                    result.append(i)
                    break
        return result