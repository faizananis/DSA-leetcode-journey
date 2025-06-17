class Solution:
    def minWindow(self,s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        window_count = defaultdict(int)
        
        have, need = 0, len(t_count)
        res = [-1, -1]
        res_len = float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_count[char] += 1

            # If the char is needed and count matches t
            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            # When all needed characters are in current window
            while have == need:
                # Update result if this window is smaller
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Now try to shrink the window
                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""

            