class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1,str2):
            if str1==str2[:len(str1)] and str1==str2[-len(str1):]:
                return True
            return False
        
        count=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i],words[j]):
                    count+=1

        return count
