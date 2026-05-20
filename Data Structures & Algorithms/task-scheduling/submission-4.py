class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        freqs = {}

        for task in tasks:
            freqs[task] = freqs[task] + 1 if task in freqs else 1
        
        for key in freqs:
            heapq.heappush_max(heap, freqs[key])

        cycles = 0
        q = deque()
        
        while heap or q:
            cycles += 1

            if heap:
                curr = (heapq.heappop_max(heap)) - 1
                if curr:
                    q.append([curr, cycles + n])
                
            if q and q[0][1] == cycles:
                heapq.heappush_max(heap, q.popleft()[0])

        return cycles