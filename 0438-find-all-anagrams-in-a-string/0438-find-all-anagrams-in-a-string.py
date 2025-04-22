class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        p_freq=Counter(p)
        # for c in p:
        #     if c not in p_freq:
        #         p_freq[c]=1
        #     else:
        #         p_freq[c]+=1
        
        left=0
        right=0
        window={}
        ans=[]

        for right in range(len(s)):
            if s[right] not in window:
                window[s[right]]=1
            else:
                window[s[right]]+=1

            if (right-left+1)<len(p):
                continue
            elif right-left+1==len(p):
                if window==p_freq:
                    ans.append(left)
            else:
                window[s[left]]-=1
                if window[s[left]]==0:
                    del window[s[left]]
                left+=1
                if window==p_freq:
                    ans.append(left)
        return ans
