class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        st=[]
        score=0
        word=""
        maximum=0
        minimum=0
        if x>y:
            word="ab"
            maximum=x
            minimum=y
        else:
            word="ba"
            maximum=y
            minimum=x
        for i in range(len(s)):
            if st and st[-1]==word[0] and s[i]==word[1]:
                st.pop()
                score+=maximum
            else:
                st.append(s[i])
        word=word[::-1]
        stack=[]
        for i in range(len(st)):
            if stack and stack[-1]==word[0] and st[i]==word[1]:
                stack.pop()
                score+=minimum
            else:
                stack.append(st[i])
        return score