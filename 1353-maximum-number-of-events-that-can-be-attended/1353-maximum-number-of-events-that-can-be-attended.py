class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n=len(events)
        day=events[0][0]
        heap=[]
        ans=0
        i=0
        while heap or i<n:
            if not heap:
                day=events[i][0]
            while i<n and events[i][0]==day:
                heapq.heappush(heap,events[i][1])
                i+=1
            if heap:
                heapq.heappop(heap)
                ans+=1
            day+=1
            while heap and heap[0]<day:
                heapq.heappop(heap)
        return ans

                