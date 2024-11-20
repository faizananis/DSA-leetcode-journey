class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        freq = [0] * 3  
        left = 0
        while left < n and (freq[0] < k or freq[1] < k or freq[2] < k):
            freq[ord(s[left]) - ord('a')] += 1
            left += 1

        # If it's impossible to satisfy the condition
        if freq[0] < k or freq[1] < k or freq[2] < k:
            return -1

        # Initialize shortest valid segment
        shortest = left
        left -= 1
        right = n - 1

        # Shrink the left window and adjust the right pointer
        while left >= 0:
            freq[ord(s[left]) - ord('a')] -= 1
            left -= 1

            # Expand the right pointer if the condition is violated
            while left <= right and (freq[0] < k or freq[1] < k or freq[2] < k):
                freq[ord(s[right]) - ord('a')] += 1
                right -= 1

            # Update shortest valid segment
            shortest = min(shortest, n - (right - left))

        return shortest