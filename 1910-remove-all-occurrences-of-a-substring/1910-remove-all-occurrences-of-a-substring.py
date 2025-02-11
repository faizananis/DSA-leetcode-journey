class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n=len(part)
        flag=True
        while flag:
            flag=False
            count=0
            st=[]
            for ch in s:
                st.append(ch)
                if ch==part[count]:
                    count+=1
                elif ch==part[0]:
                    count=1
                else:
                    count=0
                if count==n:
                    flag=True
                    for _ in range(n):
                        st.pop()
                    count=0
        return "".join(st)

