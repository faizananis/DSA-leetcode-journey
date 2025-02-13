class Solution:
    def minOperations(self, nums, k):
        # Create a min-heap using heapq
        minheap = []
        for num in nums:
            heapq.heappush(minheap, num)  # Add all elements to the heap
        
        count = 0  # Counter for the number of operations
        while minheap:
            min1 = heapq.heappop(minheap)  # Get the smallest element
            if min1 >= k:
                break  # If the smallest element is >= k, stop
            min2 = heapq.heappop(minheap)  # Get the second smallest element
            # Push the new element into the heap
            heapq.heappush(minheap, 2 * min(min1, min2) + max(min1, min2))
            count += 1  # Increment the operation count
        return count
