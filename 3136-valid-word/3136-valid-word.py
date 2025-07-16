class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        alpha=False
        vowel=False
        my_dict={'a','e','i','o','u','A','E','I','O','U'}
        for n in word:
            if n.isalpha() or n.isdigit():
                if n in my_dict:
                    vowel=True
                elif n.isalpha():
                    alpha=True
            else:
                return False
        return alpha and vowel
