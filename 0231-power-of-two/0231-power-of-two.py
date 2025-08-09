class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        st=bin(n)
        if st.count('1')==1 and n>=0:
            return True
        return False