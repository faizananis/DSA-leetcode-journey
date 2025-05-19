class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        # Step 2: Use a max heap (use negative values for max behavior)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)

        time = 0

        while max_heap:
            i = 0
            temp = []

            # Step 3: Pick up to n + 1 tasks in one round
            while i <= n:
                if max_heap:
                    count = heapq.heappop(max_heap)
                    if count < -1:
                        temp.append(count + 1)  # decrease count
                time += 1
                if not max_heap and not temp:
                    break  # All tasks done
                i += 1

            # Step 4: Push remaining tasks back to heap
            for item in temp:
                heapq.heappush(max_heap, item)

        return time