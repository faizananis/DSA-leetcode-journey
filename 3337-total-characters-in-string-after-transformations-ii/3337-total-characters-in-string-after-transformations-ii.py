class Solution:
    MOD = 10**9 + 7

    def matrix_multiply(self, A, B):
        size = 26
        result = [[0] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % self.MOD
        return result

    def matrix_exponentiate(self, base, exponent):
        size = 26
        # Identity matrix
        result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

        while exponent > 0:
            if exponent % 2 == 1:
                result = self.matrix_multiply(result, base)
            base = self.matrix_multiply(base, base)
            exponent //= 2

        return result

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # Step 1: Frequency count of characters in string
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Step 2: Build transformation matrix
        T = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for add in range(1, nums[i] + 1):
                T[(i + add) % 26][i] += 1

        # Step 3: Raise matrix T to power t
        T_powered = self.matrix_exponentiate(T, t)

        # Step 4: Multiply matrix with frequency vector
        updated_freq = [0] * 26
        for i in range(26):
            for j in range(26):
                updated_freq[i] = (updated_freq[i] + T_powered[i][j] * freq[j]) % self.MOD

        # Step 5: Sum all frequencies to get the final length
        return sum(updated_freq) % self.MOD
        