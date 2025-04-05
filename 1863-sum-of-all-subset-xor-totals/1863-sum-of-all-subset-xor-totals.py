class Solution:
    def subsetXORSum(self, nums):
        def solve(i, curr_subset):
            if i == len(nums):
                subsets.append(curr_subset[:])
                return
            
            # Include nums[i]
            curr_subset.append(nums[i])
            solve(i + 1, curr_subset)
            
            # Exclude nums[i]
            curr_subset.pop()
            solve(i + 1, curr_subset)
        
        subsets = []
        solve(0, [])

        result = 0
        for subset in subsets:
            xor_val = 0
            for num in subset:
                xor_val ^= num
            result += xor_val

        return result
