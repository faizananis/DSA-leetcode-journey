import math

class Solution:
    def canAssign(self, nums, max_val, operations):
        count = 0
        for ele in nums:
            if ele > max_val:
                count += math.ceil((ele - max_val) / max_val)
        return count <= operations

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low, high = 1, max(nums)
        res = float('inf')

        while low <= high:
            mid = low + (high - low) // 2
            if self.canAssign(nums, mid, maxOperations):
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res