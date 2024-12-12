import math
import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-x for x in gifts]
        heapq.heapify(gifts)
        for i in range(k):
            num=heapq.heappop(gifts)
            heapq.heappush(gifts,-math.floor(math.sqrt(-num)))
        return -sum(gifts)
        