class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks_with_index = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        
        # Sort by enqueueTime
        tasks_with_index.sort()
        
        result = []             # Final task processing order
        heap = []               # Min-heap for available tasks
        time = 0                # Current CPU time
        i = 0                   # Pointer to tasks_with_index

        n = len(tasks)
        
        while i < n or heap:
            # Step 1: Push all available tasks into heap
            while i < n and tasks_with_index[i][0] <= time:
                enqueueTime, processingTime, index = tasks_with_index[i]
                heapq.heappush(heap, (processingTime, index))
                i += 1

            # Step 2: If no task is available, jump time to next task's enqueue time
            if not heap:
                time = tasks_with_index[i][0]
                continue

            # Step 3: Pick the best task from heap
            processingTime, index = heapq.heappop(heap)
            time += processingTime
            result.append(index)

        return result