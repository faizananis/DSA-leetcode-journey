class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_freq={}
        for c in p:
            if c not in p_freq:
                p_freq[c]=1
            else:
                p_freq[c]+=1
        
        left=0
        right=0
        window={}
        ans=[]
        
        while right<len(p):
            if s[right] not in window:
                window[s[right]]=1
            else:
                window[s[right]]+=1
            right+=1
        
        if window==p_freq:
            ans.append(left)

        for right in range(len(p),len(s)):
            window[s[left]]-=1
            if window[s[left]]==0:
                del window[s[left]]
            left+=1
            if s[right] not in window:
                window[s[right]]=1
            else:
                window[s[right]]+=1
            if window==p_freq:
                ans.append(left)
        return ans
