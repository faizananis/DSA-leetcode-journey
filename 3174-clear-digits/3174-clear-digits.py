class Solution:
    def clearDigits(self, s: str) -> str:
        st=[]
        for ch in s:
            if ord(ch)>=97 and ord(ch)<=122:
                st.append(ch)
            elif st:
                st.pop()
        return "".join(st)