class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_len = 0
        
        # Try for every possible number of unique characters (1 to 26)
        for unique_target in range(1, 27):
            left = 0
            right = 0
            freq = [0] * 26  # frequency of each character
            unique = 0       # current unique characters in window
            count_at_least_k = 0  # how many characters have freq >= k

            while right < len(s):
                # Expand the window
                if unique <= unique_target:
                    idx = ord(s[right]) - ord('a')
                    if freq[idx] == 0:
                        unique += 1
                    freq[idx] += 1
                    if freq[idx] == k:
                        count_at_least_k += 1
                    right += 1
                else:
                    # Shrink the window
                    idx = ord(s[left]) - ord('a')
                    if freq[idx] == k:
                        count_at_least_k -= 1
                    freq[idx] -= 1
                    if freq[idx] == 0:
                        unique -= 1
                    left += 1

                # If all unique characters appear at least k times
                if unique == count_at_least_k:
                    max_len = max(max_len, right - left)

        return max_len

        