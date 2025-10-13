class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        my_dict={}
        st=[]
        for word in words:
            if not st:
                st.append(word)
                my_dict=Counter(word)
            elif st and my_dict==Counter(word):
                continue
            else:
                my_dict=Counter(word)
                st.append(word)
        return st