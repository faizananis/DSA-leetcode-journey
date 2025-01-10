class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # STEP-1: Find freq of every word in words2
        freq_words2 = [0] * 26
        for word in words2:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            freq_words2 = [max(freq_words2[i], freq[i]) for i in range(26)]

        # STEP-2: Find universal words in words1
        universal_words = []
        for word in words1:
            freq_word = [0] * 26
            for c in word:
                freq_word[ord(c) - ord('a')] += 1
            if all(freq_word[i] >= freq_words2[i] for i in range(26)):
                universal_words.append(word)
        return universal_words


        # result=[]
        # subFreq=[0]*26
        # for word in words2:
        #     for char in word:
        #         subFreq[ord(char)-ord('a')]+=1
        
        # for word in words1:
        #     freq=[0]*26
        #     for char in word:
        #         freq[ord(char)-ord('a')]+=1
        #     for i in range(26):
        #         if freq[i]==subFreq[i]==0:
        #             continue
        #         if freq[i]>subFreq[i]:
        #             break
        #     else:
        #         result.append(word)
        
        # return result
