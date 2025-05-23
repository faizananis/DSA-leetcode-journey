class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total_sum = 0
        count = 0
        min_loss = float('inf')  # Like INT_MAX

        for num in nums:
            xor_val = num ^ k

            if xor_val > num:
                total_sum += xor_val
                count += 1
            else:
                total_sum += num

            min_loss = min(min_loss, abs(num - xor_val))

        # If number of replaced elements is even, all good
        if count % 2 == 0:
            return total_sum
        else:
            return total_sum - min_loss

        