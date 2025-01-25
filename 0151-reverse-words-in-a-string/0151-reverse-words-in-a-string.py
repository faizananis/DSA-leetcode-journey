class Solution:
    def reverseWords(self, s: str) -> str:
        my_string=s.strip().split()
        my_string=reversed(my_string)
        result=""
        for string in my_string:
            result+=string
            result+=" "
        return result.rstrip()
