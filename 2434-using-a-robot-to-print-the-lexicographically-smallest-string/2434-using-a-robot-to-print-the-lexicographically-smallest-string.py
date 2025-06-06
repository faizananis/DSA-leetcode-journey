class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        
        # Build the suffix array to store minimum characters to the right
        minCharToRight = [''] * n
        minCharToRight[-1] = s[-1]
        
        for i in range(n - 2, -1, -1):
            minCharToRight[i] = min(s[i], minCharToRight[i + 1])
        
        t = []
        paper = []
        
        i = 0
        while i < n:
            t.append(s[i])
            minChar = minCharToRight[i + 1] if i + 1 < n else s[i]
            
            while t and t[-1] <= minChar:
                paper.append(t.pop())
            
            i += 1
        
        # Append remaining characters from t to paper
        while t:
            paper.append(t.pop())
        
        return ''.join(paper)