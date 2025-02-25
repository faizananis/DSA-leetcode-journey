class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1  # Prefix sum of 0 is even
        total = 0
        prefix_sum = 0

        for ele in arr:
            prefix_sum += ele
            if prefix_sum % 2 == 1:  # If prefix sum is odd
                total = (total + even_count) % MOD
                odd_count += 1
            else:  # If prefix sum is even
                total = (total + odd_count) % MOD
                even_count += 1
        return total