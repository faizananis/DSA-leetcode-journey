class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        my_dict={'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for c in text:
            if c in my_dict:
                my_dict[c]+=1
        ans=float("inf")
        for key in my_dict:
            if key=='l' or key=='o':
                ans=min(ans,my_dict[key]//2)
            else:
                ans=min(ans,my_dict[key])
        return ans