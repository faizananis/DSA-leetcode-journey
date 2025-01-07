class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result=[]
        for i in words:
            for j in words:
                if i==j:
                    continue
                if i in j:
                    result.append(i)
                    break
        return result