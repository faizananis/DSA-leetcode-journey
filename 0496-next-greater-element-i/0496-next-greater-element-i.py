class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []  # This will store numbers in decreasing order (monotonic stack)
        next_greater_map = {}  # This will map each number in nums2 to its next greater element

        # Step 1: Go through each number in nums2
        for num in nums2:
            # Check if current number is greater than the top of the stack
            # If it is, we found the next greater element for stack[-1]
            while stack and num > stack[-1]:
                smaller_num = stack.pop()
                next_greater_map[smaller_num] = num  # Store the next greater element
            # Push the current number onto the stack
            stack.append(num)

        # Step 2: For numbers left in the stack, there is no next greater element
        while stack:
            smaller_num = stack.pop()
            next_greater_map[smaller_num] = -1  # Assign -1 because no greater element exists

        # Step 3: Build the result for nums1 using the precomputed map
        result = []
        for num in nums1:
            result.append(next_greater_map[num])  # Look up the next greater element

        return result