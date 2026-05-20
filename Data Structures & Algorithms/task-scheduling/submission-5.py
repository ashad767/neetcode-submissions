class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = list(counts.values())
        heapq.heapify_max(heap)
        
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