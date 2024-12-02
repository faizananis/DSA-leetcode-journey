class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words=sentence.split()
        for i in range(len(words)):
            if len(words[i])<len(searchWord):
                continue
            for j in range(len(searchWord)):
                if searchWord[j]!=words[i][j]:
                    break
            else:
                return i+1
        return -1
