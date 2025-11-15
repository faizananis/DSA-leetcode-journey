class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # left=0
        # right=0
        # n=len(s)
        # count=0
        # arr=[0,0]
        # while right<n:
        #     if s[right]=='1':
        #         arr[1]+=1
        #     else:
        #         arr[0]+=1
        #     if arr[1]>=arr[0]**2:
        n = len(s)
        pre = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == "0":
                pre[i + 1] = i
            else:
                pre[i + 1] = pre[i]

        res = 0
        for i in range(1, n + 1):
            cnt0 = 1 if s[i - 1] == "0" else 0
            j = i
            while j > 0 and cnt0 * cnt0 <= n:
                cnt1 = (i - pre[j]) - cnt0
                if cnt0 * cnt0 <= cnt1:
                    res += min(j - pre[j], cnt1 - cnt0 * cnt0 + 1)
                j = pre[j]
                cnt0 += 1
        return res