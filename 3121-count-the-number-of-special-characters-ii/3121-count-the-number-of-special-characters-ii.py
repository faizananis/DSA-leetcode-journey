class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        my_dict={}
        count=0
        for i in range(len(word)):
            if word[i] not in my_dict:
                my_dict[word[i]]=[i]
            else:
                my_dict[word[i]].append(i)
        
        for key in my_dict:
            if ord(key)<97 and chr(ord(key)+32) in my_dict:
                if my_dict[chr(ord(key)+32)][-1]<my_dict[chr(ord(key))][0]:
                    count+=1
        return count
