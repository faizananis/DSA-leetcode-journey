class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st=[]
        n=len(pushed)
        push=0
        pop=0
        while push<n or pop<n:
            if st and pop<n and popped[pop]==st[-1]:
                st.pop()
                pop+=1
            elif push<n:
                st.append(pushed[push])
                push+=1
            else:
                break
        return push==pop==n
            