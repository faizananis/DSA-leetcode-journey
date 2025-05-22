class Solution:
    def maxRemoval(self, nums, queries):
        n = len(nums)

        # Min-heap for past used queries (end indices)
        past = []
        
        # Max-heap for available queries (store negative to simulate max-heap)
        max_heap = []

        # Sort queries by start index
        queries.sort()

        j = 0  # Pointer for queries
        used_count = 0

        for i in range(n):
            # Push all queries that start at i into max_heap
            while j < len(queries) and queries[j][0] == i:
                # Push negative to simulate max-heap
                heapq.heappush(max_heap, -queries[j][1])
                j += 1

            # Reduce nums[i] by the number of active past queries
            nums[i] -= len(past)

            # Try to apply more queries from the max heap
            while nums[i] > 0 and max_heap and -max_heap[0] >= i:
                r = -heapq.heappop(max_heap)
                heapq.heappush(past, r)
                used_count += 1
                nums[i] -= 1

            if nums[i] > 0:
                return -1

            # Remove expired queries
            while past and past[0] == i:
                heapq.heappop(past)

        return len(queries) - used_count
 