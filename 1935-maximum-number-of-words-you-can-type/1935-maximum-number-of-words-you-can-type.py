class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        my_set=set(brokenLetters)
        count=0
        flag=True
        for i in range(len(text)):
            if text[i] in my_set:
                flag=False
            if text[i]==' ' and text[i-1]!=' ' and flag==True:
                count+=1
            elif text[i]==' ':
                flag=True
        if flag==True:
            count+=1
        return count

            
                
                